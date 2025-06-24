@echo off
:: Prompt for the filename
set /p filename=Enter the Python file name (without .py): 

:: Full path to the source file
set src=unsaved\%filename%.py

:: Check if the file exists
if not exist "%src%" (
    echo ❌ File not found: %src%
    pause
    exit /b
)

:: Prompt for commit message
set /p msg=Enter a short commit message: 

:: Create the destination folder if it doesn't exist
mkdir "problems\%filename%" 2>nul

:: Move the file to the folder
move "%src%" "problems\%filename%"

:: Git operations
git add "problems\%filename%"
git commit -m "%msg%"
git push origin main

echo ✅ Successfully committed: %filename%.py
pause