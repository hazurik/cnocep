from colorama import Fore, Style, init
from termcolor import colored
from requests import get
import os
import platform
import pystyle
import random
import string

clr = """
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
"""
exec(clr)

mailgen = """
def generate_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com", "mail.ru", "yandex.ru", "hotmail.com"]
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(username_length))
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email

# Пример использования
print("Сгенерированный email:", generate_email())
"""

passgen = """
def generate_password(length):
    if length < 1:
        return "Длина пароля должна быть положительным числом"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Пример использования
length = int(input("Введите длину пароля: "))
exec(clr)
print("Сгенерированный пароль:", generate_password(length))
"""



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
    ║          [1] FSnos         [3] Генератор паролей       ║
    ║          [2] DBHack        [4] Генератор почт          ║
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

if choice == "3":
    exec(passgen)

if choice == "4":
    exec(clr)
    exec(mailgen)