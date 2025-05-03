@echo off
:: Set color for the command prompt (e.g., green text on black background)
color 0a

:: Set the working directory
cd /d D:\python\projects\app_checking

:: Activate the virtual environment
call D:\python\projects\app_checking\.venv\Scripts\activate

:: Run the Python script
python run.py

:: Keep the "hacking" vibe going with an additional message
echo.
echo [INFO] Script executed successfully. Checking app versions...
echo.

:: End the script
@REM script to check apps updated version (created by Alisher)
