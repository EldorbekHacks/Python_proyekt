# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:08:53 2025

@author: Eldorbek
"""

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha tasodifiy son o'yladim. Topaolsizmi?\n")
    taxminlar = 0
    
    while True:
        taxmin =int(input("Sizning javobingiz: "))
        taxminlar+=1
        if taxmin<tasodifiy_son:
            print("Men o'ylagan son bundan kattaroq.yana xarakat qilib ko'ring.")
        elif taxmin>tasodifiy_son:
            print("Men o'ylagan son bundan kichikroq.yana xarakat qilib ko'ring.")
        else:
            break
    print(f"Tabriklaymiz Men o'ylagan sonni siz {taxminlar} ta taxmin bilan topdingiz\n")
    return taxminlar




def sontop_pc(x=10):
    input(f"Endi Siz 1 dan {x} gacha istalgan son o'ylang va enter tugmasini bosing. Man topaman:\n >>> ")
    min = 1
    max = x
    taxminlar = 0
    while True:
        taxminlar +=1
        if min != max:
            taxmin = random.randint(min, max)
        else:
            taxmin = min
        javob = input(f"Siz o'ylagan son {taxmin}. Agar to'g'ri bo'sa (t), siz o'ylagan son bu sondan katta bo'lsa (+), agarda kichikroq bo'lsa(-), tugmalarini bosing. \n".lower())
        if javob == ('-'):
            max = taxmin-1
        elif javob == ('+'):
            min = taxmin+1
        else:
            break
        
    print(f"Men siz o'ylagan sonni {taxminlar} ta taxmin bilan topdim!\n")    
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_User = sontop()
        taxminlar_Pc = sontop_pc()
        if taxminlar_User>taxminlar_Pc:
            print("Men yutdim!!\n")
        elif taxminlar_User<taxminlar_Pc:
            print("Tabriklayman Siz yutdingiz\n")
        else:
            print("Do'stlik G'alaba qozondi!")
        yana = int(input(f"yana o'ynamoqchimisz? ha(1)/ yo'q(0)\n >>> "))
        
play()