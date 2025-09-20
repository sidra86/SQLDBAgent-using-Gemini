@echo off
REM SQL Agent CLI - Windows Batch File
REM This file makes it easy to run the CLI on Windows

echo ========================================
echo SQL Agent CLI - Windows Launcher
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "cli.py" (
    echo ERROR: cli.py not found
    echo Please run this from the SQLAgent directory
    pause
    exit /b 1
)

REM Run the CLI with all arguments passed through
python cli.py %*

REM Keep window open if there was an error
if errorlevel 1 (
    echo.
    echo Command failed with error code %errorlevel%
    pause
)
