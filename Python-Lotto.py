import random
print ("..:::PYTHON-LOTTO:::..")
print ("Hi! Do you wanna play Lotto?")
print (" ")
print ("Pick:")
print ("1. YES! LETS'GO")
print ("2. Sorry :( I can't now maybe later.")

answer = input("What is your choice: ")

if answer == '1':
    ileLiczb = 6
    maksLiczba = 49

    liczby = []
    i = 0
    while i < ileLiczb:
        liczba=random.randint(1,maksLiczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    print(" ")
    print("Wytypuj", ileLiczb,"z",maksLiczba,"liczb: ")
    print(" ")
    typy=set()
    i = 0
    while i < ileLiczb:
        typ=int(input("Podaj liczbe %s: " % (i+1)))
        if typ not in typy:
            typy.add(typ)
            i = i+1
            print("twoje liczby: ", typy)
            print(" ")
    print(" ")
    print("Wylosowane liczby to:", liczby)

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        print("GRATULUJE!!! TRAFIONE LICZBY: ", trafione,)
    else:
        print("Przykro mi! Nie trafiłeś żadnej liczby :( Powodzenia następnym razem!")
else:
    print("Ok! See you soon!  :D")
