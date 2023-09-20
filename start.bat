#if python is not installed then install it
if not exist C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python39 (
    echo Installing Python...
    #download the python file to install python
    curl -o python-3.9.6-amd64.exe https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe
    #install python
    python-3.9.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    #delete the python file
    del python-3.9.6-amd64.exe
    echo Python installed!
)

#if this is the first time running start then install python requirements from requirements.txt
if not exist venv (
    python -m venv venv
    venv\Scripts\pip install -r requirements.txt
)
#activate the virtual environment
venv\Scripts\activate

#ask the user if he wants to run the dbmanager or script
echo Do you want to run the dbmanager or script?
echo 1. dbmanager
echo 2. script
set /p choice=

#if the user chooses dbmanager then run dbmanager.py
if %choice%==1 (
    venv\Scripts\python dbmanager.py
)

#if the user chooses script then run script.py
if %choice%==2 (
    venv\Scripts\python script.py
)

#deactivate the virtual environment
venv\Scripts\deactivate

