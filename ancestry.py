'''
ancestry.py: Skapa ditt släktträd!

__author__  = "Viktor Johansson Nygren"
__version__ = "1.0.0"
__email__   = "viktor.jonanssonnygren@elev.ga.ntig.se"
'''

from msvcrt import getwch
import os
from time import sleep
def remove(): #funktion för att ta bort saker från en lista
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

def add(): #funktion för att lägga till saker i listan
    x=input("Vad vill du lägga till i släktträdet\n")
    os.system('cls')
    if x in ancestry: #kollar om användarens val finns i listan
        while True:
            print(f"""{x} finns redan i ditt släktträd, vill du ändå lägga till det?
Ja(Y)
Nej(N)""")
            answer=getwch().upper() #kollar om användaren 
            if answer == "Y":
                os.system('cls')
                ancestry.append(x)
                break
            elif answer == "N":
                os.system('cls')
                break
            else:
                print("Y eller N")
    else:
        ancestry.append(x)

def sortera(): #funktion för att sortera listan
    if len(ancestry) == 0: #kollar ifall listan är tom
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
        ancestry.sort() #sorterar listan

def edit():
    print("Vad vill du ändra i släktträdet?")
    editChoice=getwch().upper() #användaren väljer vart i listan
    try:
        editChoice=int(editChoice)
    except:
        os.system('cls')
        print("Du måste skriva ett nummer när du väljer vad i listan du vill ändra")
        sleep(2)
    newName=input("Vad vill du ändra det till\n") #användaren väljer vad det nya namnet ska vara i listan
    ancestry[int(editChoice)-1]=newName #byter ut till vad användaren skrev in
    
ancestry=[] #skapar listan som man lägger in användarens val i

while True:
    os.system('cls')
    nummer=1
    print("Ditt släktträd")
    for x in ancestry: #skriver ut hela listan med allt innehåll och vilken position de har i släktträdet
        print(nummer, x)
        nummer+=1
    print("")
    print(f"Du har {nummer-1} personer i ditt släktträd") #skriver ut hur många personer man har i släktträdet
    print("")
    print("""Hur vill du redigera ditt släktträd
Lägg till/a
Ta bort/r
Redigera/e
Sortera/s
Avsluta/q\n""")
    nummer=1
    y=getwch().upper() #tar användarens knapptryck så de kan välja vad de vill göra
    if y.upper() == "A":
        os.system('cls')
        add() #starta funktionen för att lägga till något i listan
    elif y.upper() == "R":
        if len(ancestry) == 0: #kollar om listan är tom så när någon ska ta bort
            os.system('cls')
            print("Du kan inte ta bort från en lista som inte har någonting i sig")
            sleep(2)
        else:
            os.system('cls')
            remove() #starta funktionen för att ta bort någonting från listan
    elif y.upper() == "E":
        if len(ancestry) == 0: #kollar om listan är tom så när någon ska ta bort
            os.system('cls')
            print("Du kan inte ändra en lista utan någonting i")
            sleep(2)
        else:
            os.system('cls')
            for x in ancestry: #skriver ut hela listan med allt innehåll och vilken position de har i släktträdet
                print(nummer, x)
                nummer+=1
            edit() #starta funktionen för att redigera någonting från listan
    elif y.upper() == "Q":
        print("Hej då!")
        exit()
    elif y.upper() == "S": 
        os.system('cls')
        sortera() #starta funktionen för att sortera listan
    else: #om man klickar på en knapp som inte gör något så får man välja igen
        os.system('cls')
        print("Välj hur du vill redigera listan")
        sleep(2)