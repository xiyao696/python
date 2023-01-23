import time
q = int(input("Co potrzebujesz obliczyc: [1. objetosci 2. pola podstawy 3. wysokosci] "))
time.sleep(1)
#wybierasz 1-3 // wybranie powyzej 3 konczy sie errorem
if q == 1:
    print("Objetosc!")
    p = int(input("Podaj pole podstawy: "))
    h = int(input("Podaj wysokosc: "))
    v = p * h #obliczanie wartosci V (objetosci)
    print("V = Pp * H") #wzor
    time.sleep(1)
    print("Objetosc wynosi: ", v) #obliczenie
    time.sleep(20)
if q == 2:
    print("Pole podstawy!")
    v = int(input("Podaj objetosc: "))
    h = int(input("Podaj wysokosc: "))
    p = v / h #obliczanie wartosci Pp (pola podstawy)
    print("Pp = V / H") #wzor
    time.sleep(1)
    print("Pole podstawy wynosi: ", p) #obliczenie
    time.sleep(20)
if q == 3:
    print("Wysokosc!")
    v = int(input("Podaj objetosc: "))
    p = int(input("Podaj pole podstawy: "))
    h = v / p #obliczanie wartosci H (wysokosci)
    print("h = v / p") #wzor
    time.sleep(1)
    print("Wysokosc wynosi: ", h) #obliczenie
    time.sleep(20)
else: 
    print("ERROR")