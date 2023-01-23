def minimum(n):
    for i in range(n):
        a = int(input("Podaj liczbe: "))
        if i == 0:
            min = a
        else:
            if a < min:
                min = a
    return min

liczba_elementow = int(input("Podaj lczbe elementow: "))
najmniejszy = minimum(liczba_elementow)
print("Maksimum wynosi: ", najmniejszy)

input("\n\nKliknij aby zakonczyc!")