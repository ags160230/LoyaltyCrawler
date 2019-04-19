REM double click to execute all tests in the /tests subfolder

REM turn off command echo
@echo off
REM execute python command pytest with the tests subfold as the path
python -m pytest tests/
REM pause after execution for user to see results
timeout /t -1