@echo off
REM run.bat - Simple launcher for GitHub Project Starter
REM WHY: Quick access without installation, double-click to run

title GitHub Project Starter

:MAIN
cls
echo.
echo ================================================
echo   GitHub Project Starter
echo ================================================
echo.

REM Check if we're in the right directory
if not exist "starter\__init__.py" (
    echo [ERROR] Run this script from project root directory
    echo.
    echo Expected structure:
    echo   project_root\
    echo     starter\
    echo     templates\
    echo     run.bat  ^<-- You are here
    echo.
    pause
    exit /b 1
)

REM Check Python installation
where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not installed
    echo.
    echo Download Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Display Python version
echo [INFO] Python version:
python --version
echo.

REM Run the application
python -m starter

REM Ask to run again
echo.
echo.
set /p choice="Run again? (y/n): "
if /i "%choice%"=="y" goto MAIN
if /i "%choice%"=="yes" goto MAIN

echo.
echo [INFO] Goodbye
timeout /t 2 >nul
exit /b 0