<#
  Starts, stops or reports on the local Open Lecture server. Used by Open-Lecture.bat and Stop-Open-Lecture.bat.

    launcher.ps1 start    reuse a running server or start one (repairing the Python env and rebuilding the UI
                          when needed), then open it in the browser
    launcher.ps1 stop     stop every Open Lecture server started from this folder
    launcher.ps1 status   say whether it is running, where, and as which process

  The server runs hidden in the background and logs to .openlecture\server.log (errors: server.err.log).
  Its PID and port are kept in .openlecture\server.lock. Set OPENLECTURE_PORT to change the preferred port,
  and OPENLECTURE_NO_BROWSER=1 to skip opening the browser.
  Exit code 0 = success, 1 = failure (the .bat files keep the window open on failure).
  Keep this file ASCII-only: Windows PowerShell 5.1 reads BOM-less scripts in the ANSI code page.
#>
param([ValidateSet('start', 'stop', 'status')][string]$Command = 'start')

# 'Continue', not 'Stop': in Windows PowerShell 5.1 a native tool writing to stderr (taskkill, python, npm)
# would otherwise abort the script. Steps that must not fail silently use -ErrorAction Stop explicitly.
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $Root
$DataDir = Join-Path $Root '.openlecture'
$StateFile = Join-Path $DataDir 'server.lock'
$LogFile = Join-Path $DataDir 'server.log'
$ErrFile = Join-Path $DataDir 'server.err.log'
$WebIndex = Join-Path $Root 'src\open_lecture\web\index.html'
$VenvPy = Join-Path $Root '.venv\Scripts\python.exe'
$VenvExe = Join-Path $Root '.venv\Scripts\open-lecture.exe'
$PreferredPort = 8000
if ($env:OPENLECTURE_PORT -match '^\d+$') { $PreferredPort = [int]$env:OPENLECTURE_PORT }
$StartTimeoutSec = 150

function Say([string]$Text, [string]$Color = 'Gray') { Write-Host $Text -ForegroundColor $Color }
function Fail([string]$Text) { Say ''; Say $Text 'Red'; exit 1 }

# ------------------------------------------------------------------ helpers

function Get-Health([int]$Port, [int]$TimeoutMs = 1500) {
  # Returns the health JSON only when Open Lecture (not some other program) answers on the port.
  try {
    $req = [System.Net.HttpWebRequest]::Create("http://127.0.0.1:$Port/api/v1/health")
    $req.Proxy = $null
    $req.Timeout = $TimeoutMs
    $req.ReadWriteTimeout = $TimeoutMs
    $resp = $req.GetResponse()
    try { $body = (New-Object System.IO.StreamReader($resp.GetResponseStream())).ReadToEnd() } finally { $resp.Close() }
    $json = $body | ConvertFrom-Json -ErrorAction Stop
    if ($json.status -eq 'ok' -and $json.agent_runtime) { return $json }
  } catch {}
  return $null
}

function Test-PortFree([int]$Port) {
  try {
    $listener = New-Object System.Net.Sockets.TcpListener([System.Net.IPAddress]::Loopback, $Port)
    $listener.Start()
    $listener.Stop()
    return $true
  } catch { return $false }
}

function Get-PortOwners([int]$Port) {
  # PIDs listening on the port (Get-NetTCPConnection, falling back to netstat).
  try {
    $pids = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction Stop | Select-Object -ExpandProperty OwningProcess
    return @($pids | Where-Object { $_ -gt 0 } | Select-Object -Unique)
  } catch {
    $pids = foreach ($line in (netstat -ano -p tcp 2>$null)) {
      if ($line -match "^\s*TCP\s+\S+:$Port\s+\S+\s+LISTENING\s+(\d+)") { [int]$Matches[1] }
    }
    return @($pids | Where-Object { $_ -gt 0 } | Select-Object -Unique)
  }
}

function Test-UnderRoot([string]$Text) {
  return [bool]($Text -and $Text.IndexOf($Root, [System.StringComparison]::OrdinalIgnoreCase) -ge 0)
}

function Get-ServerProcesses {
  # Every "open-lecture serve" process started from this folder: the .exe launcher and the python it runs.
  $all = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue)
  $servers = @($all | Where-Object {
      $_.CommandLine -match 'open[-_]lecture(\.exe)?"?\s.*\bserve\b' -and
      ((Test-UnderRoot $_.CommandLine) -or (Test-UnderRoot $_.ExecutablePath))
    })
  # The venv's python.exe can hand off to the base interpreter: include children of matched processes.
  $ids = @($servers | ForEach-Object { $_.ProcessId })
  $children = @($all | Where-Object {
      $ids -contains $_.ParentProcessId -and -not ($ids -contains $_.ProcessId) -and $_.Name -ne 'conhost.exe'
    })
  return @($servers + $children)
}

function Get-Process-Safe([int]$Id) { try { return Get-Process -Id $Id -ErrorAction Stop } catch { return $null } }

function Stop-Tree([int]$Id) {
  # Killing a parent's tree can take its children first, so 'not found' here is fine.
  & cmd.exe /c "taskkill /PID $Id /T /F >nul 2>&1"
}

function Read-State {
  if (-not (Test-Path -LiteralPath $StateFile)) { return $null }
  try { return Get-Content -LiteralPath $StateFile -Raw -ErrorAction Stop | ConvertFrom-Json -ErrorAction Stop } catch { return $null }
}

function Write-State([int]$ProcessId, [int]$Port) {
  $state = [ordered]@{ pid = $ProcessId; port = $Port; url = "http://127.0.0.1:$Port"; started = (Get-Date).ToString('s') }
  $state | ConvertTo-Json | Set-Content -LiteralPath $StateFile -Encoding UTF8
}

function Find-RunningPort {
  # A healthy Open Lecture: the recorded port first, then the preferred one and its neighbours.
  $state = Read-State
  $candidates = @()
  if ($state -and $state.port) { $candidates += [int]$state.port }
  $candidates += $PreferredPort..($PreferredPort + 10)
  foreach ($port in ($candidates | Select-Object -Unique)) {
    if (-not (Test-PortFree $port) -and (Get-Health $port)) { return $port }
  }
  return $null
}

function Open-Browser([string]$Url) {
  if ($env:OPENLECTURE_NO_BROWSER) { return }  # for scripted runs and tests
  try { Start-Process $Url -ErrorAction Stop } catch { Say "Open $Url in your browser." 'Yellow' }
}

function Show-LogTail {
  foreach ($file in @($ErrFile, $LogFile)) {
    if ((Test-Path -LiteralPath $file) -and (Get-Item -LiteralPath $file).Length -gt 0) {
      Say ''
      Say "Last lines of $file :" 'Yellow'
      Get-Content -LiteralPath $file -Tail 25 | ForEach-Object { Say "  $_" }
    }
  }
}

function Lock-Launcher {
  # One launcher at a time, so a double double-click cannot start two servers.
  $mutex = New-Object System.Threading.Mutex($false, 'Local\OpenLectureLauncher')
  try { $owned = $mutex.WaitOne(180000) } catch [System.Threading.AbandonedMutexException] { $owned = $true }
  if (-not $owned) { Fail 'Another Open Lecture launcher is still busy. Try again in a minute.' }
  return $mutex
}

# ------------------------------------------------------------------ setup steps

function Find-BasePython {
  # A Python 3.12+ to (re)create the virtual environment with.
  $tries = @(@('py', '-3.13'), @('py', '-3.12'), @('python'), @('python3'))
  foreach ($t in $tries) {
    if (-not (Get-Command $t[0] -ErrorAction SilentlyContinue)) { continue }
    try {
      $args_ = @($t | Select-Object -Skip 1) + @('-c', 'import sys; print(sys.version_info >= (3, 12))')
      $out = & $t[0] @args_ 2>$null
      if ($LASTEXITCODE -eq 0 -and "$out".Trim() -eq 'True') { return , $t }
    } catch {}
  }
  return $null
}

function Test-Venv {
  if (-not ((Test-Path -LiteralPath $VenvPy) -and (Test-Path -LiteralPath $VenvExe))) { return $false }
  & $VenvPy -c 'import open_lecture.api, uvicorn' 2>$null | Out-Null
  return ($LASTEXITCODE -eq 0)
}

function Repair-Venv {
  if (Test-Venv) { return }
  Say 'Setting up the Python environment (first run or after an update; this can take a few minutes)...' 'Cyan'
  if (Get-Command uv -ErrorAction SilentlyContinue) {
    & uv sync
    if ($LASTEXITCODE -eq 0 -and (Test-Venv)) { return }
    Say 'uv sync did not work; trying plain pip instead.' 'Yellow'
  }
  $python = Find-BasePython
  if (-not $python) {
    Fail ("Python 3.12 or newer was not found.`n" +
      "Install it from https://www.python.org/downloads/ (tick 'Add python.exe to PATH'), then run this again.")
  }
  $venv = Join-Path $Root '.venv'
  if (Test-Path -LiteralPath $venv) {
    # Keep the broken one aside instead of deleting it.
    $aside = "$venv.broken-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    Say "The existing .venv does not work; moving it to $(Split-Path -Leaf $aside)." 'Yellow'
    try { Rename-Item -LiteralPath $venv -NewName (Split-Path -Leaf $aside) -ErrorAction Stop }
    catch { Fail "Could not move the broken .venv aside (is a Python window still open?): $_" }
  }
  $pyArgs = @($python | Select-Object -Skip 1) + @('-m', 'venv', $venv)
  & $python[0] @pyArgs
  if ($LASTEXITCODE -ne 0) { Fail 'Creating the virtual environment failed (see above).' }
  & $VenvPy -m pip install --disable-pip-version-check -q -e $Root
  if ($LASTEXITCODE -ne 0 -or -not (Test-Venv)) {
    Fail 'Installing Open Lecture failed (see above). Check your internet connection and run this again.'
  }
  Say 'Python environment ready.' 'Green'
}

function Get-NewestTime([string[]]$Paths) {
  $newest = [datetime]::MinValue
  foreach ($p in $Paths) {
    if (-not (Test-Path -LiteralPath $p)) { continue }
    $item = Get-Item -LiteralPath $p
    $files = if ($item.PSIsContainer) { Get-ChildItem -LiteralPath $p -Recurse -File -ErrorAction SilentlyContinue } else { @($item) }
    foreach ($f in $files) { if ($f.LastWriteTime -gt $newest) { $newest = $f.LastWriteTime } }
  }
  return $newest
}

function Update-Frontend {
  # Rebuild the interface when it is missing or older than its sources.
  $fe = Join-Path $Root 'frontend'
  if (-not (Test-Path -LiteralPath $fe)) { if (Test-Path -LiteralPath $WebIndex) { return } else { Fail 'The frontend folder is missing.' } }
  $sources = @('src', 'index.html', 'package.json', 'package-lock.json', 'vite.config.ts', 'vite.config.js', 'tsconfig.json') |
    ForEach-Object { Join-Path $fe $_ }
  $built = Test-Path -LiteralPath $WebIndex
  if ($built -and (Get-NewestTime $sources) -le (Get-Item -LiteralPath $WebIndex).LastWriteTime) { return }

  $why = if ($built) { 'The interface changed since it was last built' } else { 'First run' }
  if (-not (Get-Command npm.cmd -ErrorAction SilentlyContinue)) {
    if ($built) { Say "$why, but Node.js is not installed, so the existing build is used." 'Yellow'; return }
    Fail ("The interface has never been built and Node.js is not installed.`n" +
      'Install Node.js (LTS) from https://nodejs.org/, then run this again.')
  }
  Say "$why`: building the interface..." 'Cyan'
  Push-Location -LiteralPath $fe
  try {
    $modules = Join-Path $fe 'node_modules\.package-lock.json'
    $lock = Join-Path $fe 'package-lock.json'
    if (-not (Test-Path -LiteralPath $modules) -or
        ((Test-Path -LiteralPath $lock) -and (Get-Item -LiteralPath $lock).LastWriteTime -gt (Get-Item -LiteralPath $modules).LastWriteTime)) {
      & npm.cmd ci --no-audit --no-fund
      if ($LASTEXITCODE -ne 0) { & npm.cmd install --no-audit --no-fund }
    }
    & npm.cmd run build
    $ok = ($LASTEXITCODE -eq 0) -and (Test-Path -LiteralPath $WebIndex)
  } finally { Pop-Location }
  if (-not $ok) {
    if ($built) { Say 'The interface build failed (see above); starting with the previous build.' 'Yellow'; return }
    Fail 'Building the interface failed (see above).'
  }
  Say 'Interface built.' 'Green'
}

function Select-Port {
  if (Test-PortFree $PreferredPort) { return $PreferredPort }
  $owners = Get-PortOwners $PreferredPort
  $names = @($owners | ForEach-Object { $p = Get-Process-Safe $_; if ($p) { "$($p.ProcessName) (PID $_)" } else { "PID $_" } })
  $who = if ($names.Count) { $names -join ', ' } else { 'another program' }
  foreach ($port in ($PreferredPort + 1)..($PreferredPort + 20)) {
    if (Test-PortFree $port) {
      Say "Port $PreferredPort is taken by $who, so Open Lecture will use port $port." 'Yellow'
      return $port
    }
  }
  Fail "Ports $PreferredPort-$($PreferredPort + 20) are all taken. Close some programs or set OPENLECTURE_PORT."
}

# ------------------------------------------------------------------ commands

function Invoke-Start {
  New-Item -ItemType Directory -Force -Path $DataDir -ErrorAction Stop | Out-Null
  $mutex = Lock-Launcher
  try {
    $port = Find-RunningPort
    if ($port) {
      Say "Open Lecture is already running: http://127.0.0.1:$port" 'Green'
      Open-Browser "http://127.0.0.1:$port"
      return
    }

    # A server from this folder that is not answering: still starting (give it time) or stuck (restart it).
    $stale = @(Get-ServerProcesses)
    if ($stale.Count) {
      $youngest = ($stale | ForEach-Object { $_.CreationDate } | Sort-Object -Descending | Select-Object -First 1)
      if ($youngest -and ((Get-Date) - $youngest).TotalSeconds -lt 90) {
        Say 'Open Lecture is still starting up; waiting for it...' 'Cyan'
        for ($i = 0; $i -lt 90; $i++) {
          $port = Find-RunningPort
          if ($port) { Say "Ready: http://127.0.0.1:$port" 'Green'; Open-Browser "http://127.0.0.1:$port"; return }
          Start-Sleep -Seconds 1
        }
      }
      Say 'Found an Open Lecture server that is not responding; restarting it.' 'Yellow'
      $stale | ForEach-Object { Stop-Tree $_.ProcessId }
      Start-Sleep -Seconds 1
    }

    Repair-Venv
    Update-Frontend
    $port = Select-Port
    $url = "http://127.0.0.1:$port"

    # Keep the previous log for troubleshooting. If a log is still locked (a server we could not stop holds
    # it), write to a fresh timestamped one instead.
    foreach ($pair in @(@('LogFile', 'server.prev.log'), @('ErrFile', 'server.prev.err.log'))) {
      $path = Get-Variable -Name $pair[0] -Scope Script -ValueOnly
      if (-not (Test-Path -LiteralPath $path)) { continue }
      try { Move-Item -LiteralPath $path -Destination (Join-Path $DataDir $pair[1]) -Force -ErrorAction Stop }
      catch {
        $fresh = $path -replace '\.log$', "-$(Get-Date -Format 'yyyyMMdd-HHmmss').log"
        Set-Variable -Name $pair[0] -Scope Script -Value $fresh
      }
    }
    $env:PYTHONUNBUFFERED = '1'
    $env:PYTHONIOENCODING = 'utf-8'
    Write-Host "Starting Open Lecture on port $port (about 20-40 seconds)" -ForegroundColor Cyan -NoNewline
    # Launched through the shell (no -Redirect*/-NoNewWindow) so the server does not inherit this window's
    # handles: otherwise anything reading the launcher's output would wait until the server stopped.
    # cmd.exe writes the logs; the outer quotes are the ones cmd /c strips.
    $cmdLine = "/c `"`"$VenvExe`" serve --port $port >`"$LogFile`" 2>`"$ErrFile`"`""
    try {
      $proc = Start-Process -FilePath 'cmd.exe' -ArgumentList $cmdLine -WorkingDirectory $Root `
        -WindowStyle Hidden -PassThru -ErrorAction Stop
    } catch { Fail "Could not start the server: $_" }
    Write-State $proc.Id $port

    $deadline = (Get-Date).AddSeconds($StartTimeoutSec)
    while ((Get-Date) -lt $deadline) {
      if (Get-Health $port 1000) {
        Say ''
        Say "Open Lecture is running: $url" 'Green'
        Say 'To stop it, double-click Stop-Open-Lecture.bat.'
        Open-Browser $url
        return
      }
      if ($proc.HasExited) {
        Remove-Item -LiteralPath $StateFile -ErrorAction SilentlyContinue
        Show-LogTail
        Fail "The server stopped while starting (exit code $($proc.ExitCode)). The full log is in $DataDir."
      }
      Write-Host '.' -NoNewline
      Start-Sleep -Seconds 1
    }
    Show-LogTail
    Stop-Tree $proc.Id
    Remove-Item -LiteralPath $StateFile -ErrorAction SilentlyContinue
    Fail "The server did not answer within $StartTimeoutSec seconds, so it was stopped. See the log above."
  } finally { $mutex.ReleaseMutex(); $mutex.Dispose() }
}

function Invoke-Stop {
  $mutex = Lock-Launcher
  try {
    $targets = @{}
    foreach ($p in (Get-ServerProcesses)) { $targets[[int]$p.ProcessId] = $p.Name }
    $state = Read-State
    $ports = @($PreferredPort)
    if ($state -and $state.port) { $ports += [int]$state.port }
    # (The recorded PID is not trusted on its own: Windows reuses PIDs. Get-ServerProcesses matches the
    # actual command line, which covers it.)
    # An Open Lecture started some other way (another copy, another port) still answers its health check.
    foreach ($port in ($ports + ($PreferredPort + 1)..($PreferredPort + 10) | Select-Object -Unique)) {
      if (-not (Test-PortFree $port) -and (Get-Health $port)) {
        foreach ($id in (Get-PortOwners $port)) { $targets[[int]$id] = "listener on port $port" }
      }
    }

    if ($targets.Count -eq 0) {
      Remove-Item -LiteralPath $StateFile -ErrorAction SilentlyContinue
      Say "Open Lecture wasn't running." 'Green'
      return
    }
    foreach ($id in $targets.Keys) { Stop-Tree $id }
    for ($i = 0; $i -lt 20; $i++) {
      $left = @($targets.Keys | Where-Object { Get-Process-Safe $_ })
      if (-not $left.Count) { break }
      Start-Sleep -Milliseconds 250
    }
    Remove-Item -LiteralPath $StateFile -ErrorAction SilentlyContinue
    if (Find-RunningPort) { Fail 'Open Lecture is still answering. Close it from Task Manager (python.exe).' }
    Say 'Open Lecture stopped.' 'Green'
  } finally { $mutex.ReleaseMutex(); $mutex.Dispose() }
}

function Invoke-Status {
  $port = Find-RunningPort
  $procs = @(Get-ServerProcesses)
  if ($port) {
    $h = Get-Health $port
    Say "Running: http://127.0.0.1:$port (version $($h.version))" 'Green'
  } elseif ($procs.Count) {
    Say 'A server process exists but is not answering (starting up or stuck).' 'Yellow'
  } else {
    Say 'Not running.'
  }
  foreach ($p in $procs) { Say "  PID $($p.ProcessId): $($p.Name)" }
  Say "Log: $LogFile"
}

switch ($Command) {
  'start' { Invoke-Start }
  'stop' { Invoke-Stop }
  'status' { Invoke-Status }
}
exit 0
