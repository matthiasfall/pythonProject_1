import time

#convert different units

# varible
calc = True

# Impressum
def startscreen():
    print("********************************************"), time.sleep(0.25)
    print("*          Convert differnt units          *"), time.sleep(0.25)
    print("* Matthias Fallnbügl/092020                *"), time.sleep(0.25)
    print("*                                          *"), time.sleep(0.25)
    print("********************************************"), time.sleep(0.25)


#units to choose
    print("/n available Units - ( [1]Meter, [2]Grad Celsius, [3]KM/H, [4]Liter into [5]Fuß, [6]Grad Fahrenheit, [7]MPH, [8]Gallonen(US)" )

# functions

def meter_feet(value):
    print("Sie haben die Umrechnung Meter zu Fuß gewählt...")
    m_feet_result = float(value * 3.2808)
    print(value , " Meter sind ", round(m_feet_result, 2), " Fuß.")

def feet_meter(value):
    print("Sie haben die Umrechnung Fuß zu Meter gewählt...")
    feet_m_result = float(value / 3.2808)
    print(value, " Fuß sind ", round(feet_m_result, 2), " Meter.")

def centigrade_fahrenheit(value):
    print("Sie haben die Umrechnung Grad Celsius zu Grad Fahrenheit gewählt...")
    centigrade_fahrenheit_result = float(value * 1.8 + 32)
    print(value, " Grad Celsius sind ", round(centigrade_fahrenheit_result, 2), " Fahrenheit.")

def fahrenheit_centigrade(value):
    print("Sie haben die Umrechnung Grad Fahrenheit zu Grad Celsius gewählt...")
    fahrenheit_centigrade_result = float((value-32)* 5/9)
    print(value, " Fahrenheit sind ", round(fahrenheit_centigrade_result, 2), " Grad Celsius.")

def kmh_mph(value):
    print("Sie haben die Umrechnung KM/H zu MPH gewählt...")
    kmh_mph_result = float(value / 1.609)
    print(value, " KM/H sind ", round(kmh_mph_result, 2), " MPH.")

def mph_kmh(value):
    print("Sie haben die Umrechnung MPH zu KM/H gewählt...")
    mph_kmh_result = float(value * 1.609)
    print(value, " MPH ", round(mph_kmh_result, 2), " KM/H.")

def liter_gallons(value):
    print("Sie haben die Umrechnung Liter zu Gallonen gewählt...")
    liter_gallons_result = float(value/3.785)
    print(value, " Liter sind ", round(liter_gallons_result, 2), " Gallonen.")

def gallons_liter(value):
    print("Sie haben die Umrechnung Gallonen zu Liter gewählt...")
    gallons_liter_result = float(value * 3.8785)
    print(value, " Gallonen sind ", round(gallons_liter_result, 2), " Liter.")

#start
print(startscreen())

# userinput

while calc == True:

    choice = int(input("Geben Sie die gewünscht Einheit bekannt (1-8): "))


    # convert user input to float
    value_input = str(input("Geben Sie den Wert für die Umrechnung bekannt: "))
    value_replace = value_input.replace(",", ".")
    value = int(value_replace)




# function call

    if choice == 1:
        meter_feet(value)

    elif choice == 5:
        feet_meter(value)

    elif choice == 2:
        centigrade_fahrenheit(value)

    elif choice == 6:
        fahrenheit_centigrade(value)

    elif choice == 3:
        kmh_mph(value)

    elif choice == 7:
        mph_kmh(value)

    elif choice == 4:
        liter_gallons(value)

    elif choice == 8:
        gallons_liter(value)

    else:
        print("Bitte treffen Sie eine gültige auswahl!")

else:
    calc= input("Möchten Sie noch einen Wert umrechnen? [Y] JA oder [N] Nein: ")

