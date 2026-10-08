@echo off
rem Starts Open Lecture (or reuses the running server) and opens it in the browser.
rem Needs uv (https://docs.astral.sh/uv/) and, for the first run only, Node.js to build the UI.
setlocal
cd /d "%~dp0"
set PORT=8000
set URL=http://127.0.0.1:%PORT%

powershell -NoProfile -Command "try { (Invoke-WebRequest -UseBasicParsing -TimeoutSec 2 '%URL%/api/v1/health').StatusCode } catch { exit 1 }" >nul 2>&1
if %errorlevel%==0 (
  echo Open Lecture is already running.
  start "" %URL%
  exit /b 0
)

powershell -NoProfile -Command "if (Get-NetTCPConnection -LocalPort %PORT% -State Listen -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }" >nul 2>&1
if %errorlevel%==0 (
  echo Port %PORT% is used by another program that is not Open Lecture. Close it or edit PORT in this file.
  pause
  exit /b 1
)

if not exist "src\open_lecture\web\index.html" (
  echo First run: building the interface...
  pushd frontend
  call npm ci && call npm run build
  popd
)

echo Starting Open Lecture...
start "Open Lecture server (close this window to stop)" /min cmd /c "uv run open-lecture serve --port %PORT%"
for /l %%i in (1,1,40) do (
  powershell -NoProfile -Command "try { (Invoke-WebRequest -UseBasicParsing -TimeoutSec 1 '%URL%/api/v1/health').StatusCode } catch { exit 1 }" >nul 2>&1 && goto ready
  timeout /t 1 /nobreak >nul
)
echo The server did not start. Run "uv run open-lecture serve" to see the error.
pause
exit /b 1
:ready
start "" %URL%
