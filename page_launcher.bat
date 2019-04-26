REM turn off command echo
@echo off
REM open browser
set browser=chrome.exe
start %broswer% http://127.0.0.1:8000
REM execute webapp with runserver
python manage.py runserver
REM pass control back to command prompt afterwards
cmd