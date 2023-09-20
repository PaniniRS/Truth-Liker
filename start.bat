::if choco is not installed then install it
if not exist C:\ProgramData\chocolatey (
    powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
)
:: if python isnt installed by choco then install it using choco
if not exist C:\ProgramData\chocolatey\lib\python (
    choco install python
)

::if this is the first time running start then install python requirements from requirements.txt
if not exist venv (
    python -m venv venv
    venv\Scripts\pip install -r requirements.txt
)
::activate the virtual environment
venv\Scripts\activate

::ask the user if he wants to run the dbmanager or script
echo Do you want to run the dbmanager or script?
echo 1. dbmanager
echo 2. script
set /p choice=

::if the user chooses dbmanager then run dbmanager.py
if %choice%==1 (
    venv\Scripts\python dbmanager.py
)

::if the user chooses script then run script.py
if %choice%==2 (
    venv\Scripts\python script.py
)

::deactivate the virtual environment
venv\Scripts\deactivate

