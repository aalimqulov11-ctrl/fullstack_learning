import random
import time
import os

# Terminal ekranini tozalaymiz
os.system('clear')

# Animatsiya rangini yashil qilish uchun maxsus kod
YASHIL = "\033[32m"
OK = "\033[37m"
QIZIL = "\033[31m"

# Belgilar ro'yxati (ekranda nimalar tushishi)
belgilar = ["0", "11", "XXX", "RUSTAM", "Y", "1102", "Z", "$&", "#", "@", "%", "&", "7", "A", "B"]

try:
    while True:
        # Har bir qator uchun 80 ta tasodifiy belgi yaratamiz
        qator = ""
        for i in range(140):
            if random.random() > 0.120:
                qator += random.choice(belgilar) + " "
            else:
                qator += "  "
        
        # Ekranga yashil rangda chiqaramiz
        print(YASHIL + qator)
        
        # Animatsiya tezligi (biroz dam oladi)
        time.sleep(0.1)

except KeyboardInterrupt:
    # Ctrl + C bosilganda toza chiqib ketish uchun
    os.system('clear')
    print("Animatsiya to'xtatildi.")
