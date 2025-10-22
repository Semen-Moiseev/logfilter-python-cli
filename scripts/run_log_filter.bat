@echo off

call .venv\Scripts\activate.bat

if "%~2"=="" (
		echo Usage: %0 log_file keyword1 [keyword2 ...]
		exit /b 1
)

set LOG_FILE=%1

shift
set KEYWORDS=%*

python .\logfilter\log_filter.py "%LOG_FILE%" %KEYWORDS%
