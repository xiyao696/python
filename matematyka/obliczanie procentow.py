print("obliczanie procentow np. z sprawdzianu")

punkty = int(input("Ilosc uzyskanych punktow: "))
punktymax = int(input("Ilosc wszystkich punktow: "))

procenty = punkty * 100 // punktymax

print("Uzyskane punkty: ", punkty)
print("Wszystkie punkty: ", punktymax)
print("Ilosc procentow: ", procenty, "%")