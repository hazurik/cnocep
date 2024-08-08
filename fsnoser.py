import os
import platform

from requests import get

startapp = get("https://raw.githubusercontent.com/hazurik/cnocep/main/hwid.py").text

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')


