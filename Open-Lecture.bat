@echo off
rem Double-click: starts Open Lecture (or reuses the one already running) and opens it in your browser.
rem The server runs in the background; stop it with Stop-Open-Lecture.bat. Log: .openlecture\server.log
rem The first run sets up Python (3.12+) and builds the interface (Node.js); later runs only rebuild what changed.
setlocal
cd /d "%~dp0"
title Open Lecture
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\launcher.ps1" start
if errorlevel 1 (
  echo.
  echo Something went wrong. The details are above.
  pause
  exit /b 1
)
rem Leave the message on screen for a moment, then close.
ping -n 6 127.0.0.1 >nul
exit /b 0
