REM double click to execute all tests in the /tests subfolder

REM turn off command echo
@echo off
REM execute python command pytest with the tests subfolder as the path
python -m pytest tests/
REM execute python command pytest with the tests subfolder as the path and -s flag to allow functiong printing
python -m pytest -s tests/
REM pause after execution for user to see results
timeout /t -1