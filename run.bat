@echo off
echo Process is running...

REM Set the Python script file path
set PYTHON_SCRIPT="app.py"

REM Run the Python script
python3 %PYTHON_SCRIPT%

REM Pause to view any error messages (optional)
pause
