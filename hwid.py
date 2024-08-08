import os
import requests
import hashlib
import platform
from requests import get

clr = """
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
"""


def get_device_id():
    device_info = os.popen('cat /proc/cpuinfo').read().strip()
    return hashlib.sha256(device_info.encode()).hexdigest()

# URL, где хранятся пары HWID и пароли
hwid_url = "https://pastebin.com/raw/Rsk3d7hP"

# Получение HWID текущего устройства
hwid = get_device_id()

# Получение списка пар HWID и паролей с указанного URL
response = requests.get(hwid_url)

# Проверка HWID
access_denied = True
correct_password = None

for line in response.text.splitlines():
    if line.strip():
        parts = line.split(":")
        if len(parts) == 2:
            stored_hwid, stored_password = parts
            stored_hwid = stored_hwid.strip()
            stored_password = stored_password.strip()
            if stored_hwid.lower() == hwid.lower():
                access_denied = False
                correct_password = stored_password
                break

if access_denied:
    exec(clr)
    print("Отказано в доступе. Ваш HWID не зарегистрирован.")
else:
    exec(clr)
    input_password = input("Введите пароль: ")
    if input_password == correct_password:
        exec(clr)
        print("Пароль введен правильно. Запуск...")
        app = get("https://raw.githubusercontent.com/hazurik/cnocep/main/znozep.py").text
        exec(app)
    else:
        exec(clr)
        print("Введен неверный пароль. Доступ запрещен.")