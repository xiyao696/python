#import
import time
#obw.
print("1. trojkat")
print("2. kwadrat")
print("3. prostokat")
print("4. rownolegloboku")
print("5. romb")
print("6. trapez")
#wybor
q = int(input("ktory obwod chcesz obliczyc? : "))
#if
if q == 1:
    print("Obwod trojkata!")
    a = int(input("Podaj wartosc a: "))
    b = int(input("Podaj wartosc b: "))
    c = int(input("Podaj wartosc c: "))
    obw = a + b + c
    print("Obwod trojkata wynosi: ", obw)
    time.sleep(20)

if q == 2:
    print("Obwod kwadratu!")
    a = int(input("Podaj wartosc a: "))
    obw = a * 4
    print("Obwod kwadratu wynosi: ", obw)
    time.sleep(20)

if q == 3:
    print("Obwod prostokata!")
    a = int(input("Podaj wartosc a: "))
    b = int(input("Podaj wartosc b: "))
    obw = (a * 2) + (b * 2)
    print("Obwod prostokata: ", obw)
    time.sleep(20)

if q == 4:
    print("Obwod rownolegloboku!")
    a = int(input("Podaj wartosc a: "))
    b = int(input("Podaj wartosc b: "))
    obw = (a * 2) + (b * 2)
    print("Obwod rownolegloboku: ", obw)
    time.sleep(20)

if q == 5:
    print("Obwod rombu!")
    a = int(input("Podaj wartosc a: "))
    obw = a * 4
    print("Obwod rombu: ", obw)
    time.sleep(20)

if q == 6:
    print("Obwod trapezu!")
    a = int(input("Podaj wartosc a: "))
    b = int(input("Podaj wartosc b: "))
    c = int(input("Podaj wartosc c: "))
    d = int(input("Podaj wartosc d: "))
    obw = a + b + c + d
    print("Obwod trapeza: ", obw)
    time.sleep(20)

else:
    print("ERROR")