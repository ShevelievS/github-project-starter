@echo off
REM run.bat - Simple launcher from project root
REM WHY: No installation needed, just run

title GitHub Project Starter

REM Check if we're in the right directory
if not exist "starter\__init__.py" (
    echo [ERROR] Run this script from project root directory
    echo.
    pause
    exit /b 1
)

:MAIN
cls
echo.
echo ================================================
echo   GitHub Project Starter
echo ================================================
echo.

REM Run the application
python -m starter

REM Ask to continue
echo.
set /p choice="Run again? (y/n): "
if /i "%choice%"=="y" goto MAIN

echo [INFO] Goodbye
timeout /t 2 >nul