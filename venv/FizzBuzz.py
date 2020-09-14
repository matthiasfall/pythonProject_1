random_number = int(input("Geben Sie eine zufällige Nummer ein: "))
i = int(0)

for i in range(1, random_number+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)