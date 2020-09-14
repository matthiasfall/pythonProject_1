import random
import time
#Einleitung
print("*****************************"); time.sleep(0.5)
print("* SCHERE | STEIN | PAPIER *"); time.sleep(0.5)
print("*****************************"); time.sleep(0.5)
#Variablen
figuren = ["Schere", "Stein", "Papier"]
spielen = True
while spielen:
    #spielfiguren auswählen
    spielerauswahl = int(input("[1]Schere  [2]Stein  [3]Papier\n"))
    spielerfigur = figuren[spielerauswahl - 1]
    #Computerfigur auswählen
    computerfigur = figuren[random.randint(0, 2)]
    #Sieger ermitteln
    if spielerfigur == computerfigur:
        print("Unentschieden! Computer wählte", computerfigur)
    else:
        if spielerfigur == "Schere":
            if computerfigur == "Stein":
                print("Verloren! Computer wählte", computerfigur)
            else:
                print("Gewonnen! Computer wählte", computerfigur)
        if spielerfigur == "Stein":
            if computerfigur == "Schere":
                print("Gewonnen! Computer wählte", computerfigur)
            else:
                print("Verloren! Computer wählte", computerfigur)
        if spielerfigur == "Papier":
            if computerfigur == "Schere":
                print("Verloren! Computer wählte", computerfigur)
            else:
                print("Gewonnen! Computer wählte", computerfigur)
    #Restart?
    time.sleep(1)
    entscheidung = ""
    while entscheidung not in ("y", "n"):
        entscheidung = input("\nNochmal spielen? [y] Ja  [n]Nein")
    if(entscheidung == "n"):
        spielen = False
