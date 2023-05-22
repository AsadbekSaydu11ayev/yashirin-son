""" Yashirin son o'yini """
import random as rd
import os
print ("Assalomu alaykum! Yashirin sonlar o'yniga xush kelibsiz")
name = input("Ismingiz kim?\n>>> ")
name = name.capitalize().strip()
os.system("cls")
guess_sonlar = []

def random_son():
    sonlar = [10,15,20,25,30,35,40,45,50]
    son = rd.choice(sonlar)
    while True:
        rand = rd.randint(1,son)
        if rand is not guess_sonlar:
            guess_sonlar.append(rand)
            return rand,son

topilgan_sonlar = []
def start():
    start = input(f"Yana bir bor salom {name.capitalize()},o'yin o'ynashni istaysizmi (ha/yoq)\n>>>  ")
    if start.lower().strip() == "ha":
        while True:
            tas_son = list(random_son())
            print (f"{name} men 1 dan {tas_son[-1]} gacha son o'yladim topishga urunib ko'ring")
            string = "Son"
            urunishlar = 0
            while True:
                qaytish = 0
                try:
                    javob = int(input(f"{string} kiriting: "))
                except:
                    qaytish = 1
                    os.system("cls")
                    print (f"{name} siz butun son kiritmadingiz, iltimos boshqatdan kiritib ko'ring 😔")
                urunishlar += 1
                if qaytish == 1:
                    continue
                if javob == tas_son[0]:
                    os.system("cls")
                    print (f"Tabrikleman {name} men o'ylagan sonni {urunishlar} ta urunishda topdingiz 😃")
                    break
                elif javob < tas_son[0]:
                    os.system("cls")
                    print (f"Siz men o'ylagan sondan kichik son kiritdingiz 😔")
                    string = f"{javob} dan Kattaroq son"
                elif javob > tas_son[0]:
                    os.system("cls")
                    print (f"Siz men o'ylagan sondan katta son kiritdingiz 😔")
                    string = f"{javob} dan kichikroq son"
            print (f"{name} o'yinni davom ettirishni xohlaysizmi (ha/yoq)")
            j = input(">>> ")
            if j == "ha":
                os.system("cls")
                print (f"{name} javobingiz uchun raxmat, o'yinni davom ettiramiz 😃")
            else:
                os.system("cls")
                print (f"{name} javobingiz uchun raxmat, ko'rishguncha xayr 😃")
                break
    else:
        print (f"{name} javobingiz uchun raxmat, ko'rishguncha xayr 😃")
            
    
start()
