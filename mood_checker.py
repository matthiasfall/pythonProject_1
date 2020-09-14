print("wähle zwischen happy, nervous, sad, excited or relaxed")

mood = str(input("Wie gehts dir heute? "))

if mood == "happy":
    print("Super, dich happy zu sehen!")
elif mood == "nervous":
    print("Atme dreimal tief ein und aus.")
elif mood == "sad":
    print("Unternimm etwas das die Freude macht")
elif mood =="exited":
    print("Warum so aufgeregt")
elif mood == "relaxed":
    print("auch entspannung muss sein")
else:
    print("unbekannter Zustand!")