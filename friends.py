'''
FILNAMN.PY: Skapa ditt släktträd!

__author__  = "Viktor Johansson Nygren"
__version__ = "1.0.0"
__email__   = "viktor.jonanssonnygren@elev.ga.ntig.se"
'''

from msvcrt import getwch
import os
from time import sleep
def remove():
    y=1
    while True:
        for x in ancestry:
            print(y, x)
            y+=1
        try:
            x=int(input("Vilken i listan\n"))
            break
        except:
            print("Endast nummer")
    try:
        ancestry.pop(x-1)
        os.system('cls')
    except:
        print("Skriv nummret av namnet du vill ta bort")

def add():
    x=input("Vad vill du lägga till i släktträdet\n")
    os.system('cls')
    if x in ancestry:
        print(f"""{x} finns redan i ditt släktträd, vill du ändå lägga till det?
Ja(Y)
Nej(N)""")
        answer=getwch().upper()
        if answer == "Y":
            os.system('cls')
            ancestry.append(x)
        elif answer == "N":
            os.system('cls')
    else:
        ancestry.append(x)

def sortera():
    if len(ancestry) == 0:
        print("Du kan inte sortera en tom lista")
        sleep(2)
    else:
        os.system('cls')
        print("Listan sorteras.")
        sleep(1)
        os.system('cls')
        print("Listan sorteras..")
        sleep(1)
        os.system('cls')
        print("Listan sorteras...")
        sleep(1)
        os.system('cls')
        ancestry.sort()
        os.system('cls')

ancestry=[]

while True:
    os.system('cls')
    nummer=1
    print("Ditt släktträd")
    for x in ancestry:
        print(nummer, x)
        nummer+=1
    print("")
    print(f"Du har {nummer-1} personer i ditt släktträd")
    print("")
    print("""Hur vill du redigera ditt släktträd
Lägg till/a
Ta bort/r
Sortera/s
Avsluta/q\n""")
    y=getwch().upper()
    if y.upper() == "A":
        os.system('cls')
        add()
    elif y.upper() == "R":
        if len(ancestry) == 0:
            os.system('cls')
            print("Du kan inte ta bort från en lista som inte har någonting i sig")
            sleep(2)
        else:
            os.system('cls')
            remove()
    elif y.upper() == "Q":
        print("Hej då!")
        break
    elif y.upper() == "S":
        os.system('cls')
        sortera()
    else:
        os.system('cls')
        print("Välj någonting från listan")
        sleep(2)