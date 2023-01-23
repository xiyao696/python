import sys
import random
import time

gramy = (input("Cześć, zagramy w papier kamień nożyce? (y/n):\n"))
if gramy.lower() == "n":
    print("Trudno...")
    sys.exit(0)

print("(Jeśli zechcesz zakończyć grę wpisz '10'.)")
time.sleep(0.5)

while True:
    print()

    wybor = int(input("Wybierasz:\n1.Papier\n2.Kamień\n3.Nożyce\n"))
    wybor_komp = random.randrange(1, 3)

    if wybor == 10:
        sys.exit(0)

    if wybor == 1 and wybor_komp == 1:
        print("Papier vs Papier")
        time.sleep(0.5)
        print("Remis!")

    elif wybor == 2 and wybor_komp == 2:
        print("Kamień vs Kamień")
        time.sleep(0.5)
        print("Remis!")

    elif wybor == 3 and wybor_komp == 3:
        print("Nożyce vs Nożyce")
        time.sleep(0.5)
        print("Remis!")

    if wybor == 1 and wybor_komp == 2:
        print("Papier vs Kamień")
        time.sleep(0.5)
        print("Wygrywasz!")

    elif wybor == 2 and wybor_komp == 3:
        print("Kamień vs Nożyce")
        time.sleep(0.5)
        print("Wygrywasz!")

    elif wybor == 3 and wybor_komp == 1:
        print("Nożyce vs Papier")
        time.sleep(0.5)
        print("Wygrywasz!")

    if wybor == 1 and wybor_komp == 3:
        print("Papier vs Nożyce")
        time.sleep(0.5)
        print("Przegrywasz!")

    elif wybor == 2 and wybor_komp == 1:
        print("Kamień vs Papier")
        time.sleep(0.5)
        print("Przegrywasz!")

    elif wybor == 3 and wybor_komp == 2:
        print("Nożyce vs Kamień")
        time.sleep(0.5)
        print("Przegrywasz!")
        

    print()
    input("Wciśnij dowolny przycisk żeby grać dalej")