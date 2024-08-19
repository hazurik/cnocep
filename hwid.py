import os
import requests
import hashlib
import platform

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
hwid_url = "https://dl.dropboxusercontent.com/scl/fi/4xbmfne3vaw7qf3w6cpq3/db.txt?rlkey=7euhfngd8so3s0a1ix5g84f3f&st=1bvjjsak&dl=0"

# Получение HWID текущего устройства
hwid = get_device_id()

# Получение списка пар HWID и паролей с указанного URL
response = requests.get(hwid_url)

# Проверка HWID
access_denied = True
correct_password = None

for line in response.text.splitlines():
    if line.strip():
        parts = line.split("|")[0].split(":")  # Разделение по '|' и взятие первой части
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
        app = requests.get("https://raw.githubusercontent.com/hazurik/cnocep/main/fsbox.py").text
        exec(app)
    else:
        exec(clr)
        print("Введен неверный пароль. Доступ запрещен.")
