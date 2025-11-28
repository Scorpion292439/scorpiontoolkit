# -*- coding: utf-8 -*-
import os
import sys
import time
import random
import threading
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

# ===================== RENKLER =====================
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
M = Fore.MAGENTA + Style.BRIGHT
B = Fore.BLUE + Style.BRIGHT
RS = Style.RESET_ALL

# ===================== SES EFEKTİ (Windows) =====================
def beep():
    if sys.platform.startswith('win'):
        try:
            import winsound
            winsound.Beep(800, 200)
        except: pass

# ===================== ANIMASYONLU BAŞLANGIÇ =====================
def scorpion_intro():
    os.system("cls" if os.name == "nt" else "clear")
    logo = f"""
{R}   ███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
{R}   ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
{R}   ███████╗██║     ██║   ██║██████╔╝██████╔╝██║██║   ██║██╔██╗ ██║
{R}   ╚════██║██║     ██║   ██║██╔═══╝ ██╔═══╝ ██║██║   ██║██║╚██╗██║
{R}   ███████║╚██████╗╚██████╔╝██║     ██║     ██║╚██████╔╝██║ ╚████║
{R}   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ v3
{Style.DIM}                                  Made with blood by Scorpion292439
"""
    for line in logo.splitlines():
        print(line.center(os.get_terminal_size().columns))
        time.sleep(0.07)
    print(f"\n{M}           [ {Y}TÜRKİYE'NİN EN GÜÇLÜ TOOLKİTİ {M}]{RS}\n")
    time.sleep(1.5)
    beep()

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
                if v.get("token") == t.strip():
                    print(f"{G}   ✔ Hoş geldin {W}{v.get('email', 'Scorpion')}{G}! Token onaylandı.")
                    beep()
                    return True
        except Exception as e:
            pass
        return False

    def login(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{R}╔{'═'*68}╗")
        print(f"║{C}                     SCORPION TOOLKIT v3 - GİRİŞ PANELİ                {R}║")
        print(f"║{RS}                                                                       {R}║")
        print(f"║{Y} Token gerekli! Al → {C}{self.url}{R}                   ║")
        print(f"{R}╚{'═'*68}╝\n")
        while True:
            token_input = input(f"{C}   ╔══[ Token ]═>{G} ").strip()
            if self.check(token_input):
                self.token = token_input
                time.sleep(1.5)
                break
            print(f"{R}   ✘ Geçersiz token! Tekrar dene...\n")
            beep()

token = Token()

# ===================== ANA MENÜ =====================
def ana_menu():
    if not token.token:
        token.login()

    scorpion_intro()
    print(f"{R}   ⚠️  UYARI: Bu araç sadece eğitim ve test amaçlıdır. Kötüye kullanım sizin sorumluluğunuzdadır!{RS}\n")
    time.sleep(4)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        saat = datetime.now().strftime("%H:%M:%S")
        print(f"{M}╔{'═'*78}╗")
        print(f"║{W}   SCORPION TOOLKIT v3                {Y}[ {C}{saat} {Y}]{W}                     ║")
        print(f"║{M}╠{'═'*78}╣")
        print(f"║{W}   [{G}1{W}] SMS Bomber            {M}→{C} 100+ API ile Türkiye'nin en güçlüsü!      ║")
        print(f"║{W}   [{G}2{W}] İnsta HİT             {M}→{C} Beğeni, takipçi, hikaye izlenme aracı     ║")
        print(f"║{W}   [{G}3{W}] Hakkında                                            {Y}v3.0{R}      ║")
        print(f"║{W}   [{R}4{W}] Çıkış                                                      ║")
        print(f"{M}╚{'═'*78}╝{RS}")

        sec = input(f"\n{Y}   ╔══[ Seçim ]═>{G} ").strip()

        if sec == "1":
            try:
                import data
                data.sms_main()
            except ImportError:
                print(f"{R}   ✘ data.py bulunamadı! Aynı klasöre koyun.")
                time.sleep(2)
        elif sec == "2":
            try:
                import data2
                data2.insta_main()
            except ImportError:
                print(f"{R}   ✘ data2.py bulunamadı! Aynı klasöre koyun.")
                time.sleep(2)
            except AttributeError:
                print(f"{R}   ✘ data2.py içinde 'insta_main()' fonksiyonu yok!")
                time.sleep(2)
        elif sec == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"""
{C}   ╔══════════════════════════════════════════════════════════╗
   ║{W}                  SCORPION TOOLKIT v3                     {C}║
   ║{Y}   • Geliştirici : Scorpion292439                         {C}║
   ║{Y}   • GitHub      : scorpion292439                         {C}║
   ║{Y}   • Amaç        : Eğitim & Penetrasyon Testi             {C}║
   ║{R}   • Uyarı       : Yasal olmayan kullanım cezai yaptırımdır! {C}║
   ╚══════════════════════════════════════════════════════════╝
""")
            input(f"{Y}   Devam etmek için ENTER'a bas...")
        elif sec in ["4", "q", "exit"]:
            print(f"\n{R}   Scorpion karanlığa geri dönüyor... Görüşürüz kral! 👋\n")
            beep()
            time.sleep(1.5)
            sys.exit()
        else:
            print(f"{R}   Yanlış seçim! Lütfen 1-4 arası bir sayı girin.")
            time.sleep(1.5)

# ===================== BAŞLAT =====================
if __name__ == "__main__":
    try:
        ana_menu()
    except KeyboardInterrupt:
        print(f"\n\n{R}   Araç zorla kapatıldı. Görüşürüz kardeşim! {W}❤️")
        beep()
