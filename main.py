import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

# ===================== RENKLER =====================
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
M = Fore.MAGENTA + Style.BRIGHT

# ===================== TOKEN SİSTEMİ =====================
class Token:
    def __init__(self):
        self.url = "https://scorpion292439.github.io/scorpion-Toolkit/"
        self.verify = "https://ipchecer-default-rtdb.firebaseio.com/tokens.json"
        self.token = None

    def check(self, t):
        try:
            import requests
            data = requests.get(self.verify, timeout=10).json()
            for k, v in data.items():
                if v.get("token") == t:
                    print(f"{G} Hoş geldin {W}{v.get('email', 'Scorpion')}{G}!")
                    return True
        except: pass
        return False

    def login(self):
        os.system("clear")
        print(f"""
{R}╔══════════════════════════════════════════════════════════════════════════════╗
║
║ S̷̡̱͖͈̜͓̼͓̝̈́̚C̸͕̭̯̻̄̈́̾ͅȌ̸̟̲̋̔̈́̓͋̓͂R̶̡͖͉͔̪̦͈̣͛̐̏̉̋̽̏P̵̡̨̘͚̪͚͎̤̣̈́̋̑Į̶͙̜͍̫͚͇͑Ơ̵͚̩̮̯͖̖̹̆͒̿̈N̷̙̩̪̼̣̮̯͍̈̉̇͂́̋̈̇̄͒ ̵̢͔͚̤͍̤̺̙̭̀̐̊́̈́̒̎̓̅ͅT̶̟̝̠̘͙̻̈́̋͋Ò̶̧͙͇̳͕̲̰͈̩̀̎̂͂͝ͅO̵̢̠̳̻̐͋̎̄́̃̏̑L̸͓̞͌͒͘K̷͎̲̽İ̴͓̯͈͖̔̌̌̂Ť̵̥̹̱̱̥̬̭̩͜
║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
        print(f"{Y} Token gerekli! Al → {C}{self.url}")
        while True:
            token_input = input(f"\n{C} Token: {G}").strip()
            if self.check(token_input):
                self.token = token_input
                time.sleep(2)
                break
            print(f"{R} Geçersiz token! Tekrar dene...\n")

token = Token()

def menu():
    if not token.token:
        token.login()
    # Token doğrulandıktan sonra uyarı mesajı
    print(f"{R}⚠️  UYARI: Bu aracı kullanmak tamamen sizin sorumluluğunuzdadır. Yasal olmayan kullanımlar cezai sorumluluk doğurabilir. Scorpion Toolkit sadece eğitim amaçlıdır.{Style.RESET_ALL}")
    time.sleep(3)
    while True:
        os.system("clear")
        print(f"""
{R}╔══════════════════════════════════════════════════════════════════════════════╗
║
║ S̷̡̱͖͈̜͓̼͓̝̈́̚C̸͕̭̯̻̄̈́̾ͅȌ̸̟̲̋̔̈́̓͋̓͂R̶̡͖͉͔̪̦͈̣͛̐̏̉̋̽̏P̵̡̨̘͚̪͚͎̤̣̈́̋̑Į̶͙̜͍̫͚͇͑Ơ̵͚̩̮̯͖̖̹̆͒̿̈N̷̙̩̪̼̣̮̯͍̈̉̇͂́̋̈̇̄͒ ̵̢͔͚̤͍̤̺̙̭̀̐̊́̈́̒̎̓̅ͅT̶̟̝̠̘͙̻̈́̋͋Ò̶̧͙͇̳͕̲̰͈̩̀̎̂͂͝ͅO̵̢̠̳̻̐͋̎̄́̃̏̑L̸͓̞͌͒͘K̷͎̲̽İ̴͓̯͈͖̔̌̌̂Ť̵̥̹̱̱̥̬̭̩͜
║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
        print(f"{W}1. SMS Bomber")
        print(f"{W}2. Çıkış")
        sec = input(f"{Y} Seçim → {G}").strip()
        if sec == "1":
            try:
                import smsbomber
                smsbomber.sms_main()
            except ImportError:
                print(f"{R}Hata: smsbomber.py dosyasını bulamadı. Lütfen aynı klasöre koyun.{W}")
                time.sleep(2)
        elif sec == "2":
            print(f"{R} Scorpion kayboldu...{W}")
            sys.exit()
        else:
            print(f"{R} Geçersiz seçim!{W}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R} Araç kapatıldı.")
