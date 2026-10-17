@echo off
rem Double-click: stops the Open Lecture server (only Open Lecture; other programs on the port are left alone).
setlocal
cd /d "%~dp0"
title Stop Open Lecture
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\launcher.ps1" stop
if errorlevel 1 (
  echo.
  pause
  exit /b 1
)
ping -n 4 127.0.0.1 >nul
exit /b 0
