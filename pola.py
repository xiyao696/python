#import
import time
#pola
print("1. trojkat")
print("2. kwadrat")
print("3. prostokat")
print("4. rownolegloboku")
print("5. romb")
print("6. trapez")
#wybor
q = int(input("ktore pole chcesz obliczyc? : "))
#if
if q == 1:
    print("Pole trojkata!")
    a = int(input("Podaj wartosc a: "))
    h = int(input("Podaj wartosc h: "))
    p = a * h / 2
    print("Pole trojkata wynosi: ", p)
    time.sleep(20)

if q == 2:
    print("Pole kwadratu!")
    a = int(input("Wartosc a: "))
    p = a * a
    print("Pole kwadratu wynosi: ", p)
    time.sleep(20)

if q == 3:
    print("Pole prostokata!")
    a = int(input("Podaj wartosc a: "))
    b = int(input("Podaj wartosc b: "))
    print("Pole prostokata wynosi: ", p)
    time.sleep(20)

if q == 4:
    print("Pole rownolegloboku!")
    a = int(input("Podaj wartosc a: "))
    h = int(input("Podaj wartosc h: "))
    p = a * h
    print("Pole rownolegloboku wynosi: ", p)
    time.sleep(20)

if q == 5:
    print("Pole rombu!")
    a = int(input("Podaj wartosc a: "))
    h = int(input("Podaj wartosc h: "))
    p = a * h
    print("Pole rombu wynosi: ", p)
    time.sleep(20)
    
if q == 6:
    print("Pole trapezu!")
    a = int(input("Podaj wartosc a: "))
    b = int(input("Podaj wartosc b: "))
    h = int(input("Podaj wartosc h: "))
    p = (a + b) / 2 * h
    print("Pole trapezu wynosi: ", p)
    time.sleep(20)

else:
    print("ERROR")
    time.sleep(3)