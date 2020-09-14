import random


secret = random.randint(1, 20)
guess = int(0)
a = "ende"
status = ""


while guess != secret:
        print("errate die zahl")
        guess = int(input("Rate die Geheimzahl zwischen 1 und 20: "))
        if guess != secret:
            print("leider falsch")
        else:
            print("Du hast die zahl erraten!")
            break





