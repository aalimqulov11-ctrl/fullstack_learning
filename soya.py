import math
import time
import os
import random

# Terminalni tozalaymiz
os.system('clear')

YASHIL = "\033[32m"
OK = "\033[37m"

# Matrix belgilari
belgilar = ["0", "1", "X", "Y", "Z", "$", "#", "@", "%", "7", "RUSTAM", "XXX"]

burchak = 0.0

try:
    while True:
        # Kursorni har doim tepaga qaytaramiz
        print("\033[H", end="")
        
        # 25 qator va 100 ta ustunli katta maydon
        for y in range(-12, 13):
            qator = ""
            for x in range(-50, 50):
                # Aylanuvchi shakl formulasini hisoblaymiz
                faza = x * 0.4 * math.cos(burchak) + y * math.sin(burchak)
                
                # Agar nuqta aylanuvchi shakl chizig'iga tushsa, qalin belgi qo'yamiz
                if -1.5 < faza < 1.5:
                    qator += "█"
                elif -4 < faza < -1.5 or 1.5 < faza < 4:
                    qator += "▓"
                # Shakldan tashqaridagi bo'shliqlarga Matrix kodlarini to'ldiramiz
                else:
                    if random.random() > 0.94:
                        qator += random.choice(belgilar)
                    else:
                        qator += " "
            
            # Ekranga yashil rangda chiqaramiz
            print(YASHIL + qator)
            
        burchak += 0.15
        time.sleep(0.04)  # Tezligi

except KeyboardInterrupt:
    os.system('clear')
    print(OK + "Animatsiya to'xtatildi.")
