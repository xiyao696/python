def maksimum(n):
    for i in range(n):
        a = int(input("Podaj liczbe: "))
        if i == 0:
            maks = a
        else:
            if a < maks:
                maks = a
    return maks

liczba_elementow = int(input("Podaj lczbe elementow: "))
najwiekszy = maksimum(liczba_elementow)
print("Maksimum wynosi: ", najwiekszy)

input("\n\nKliknij aby zakonczyc!")