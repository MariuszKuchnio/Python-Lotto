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
    print("\nPredict", ileLiczb,"from",maksLiczba,"numbers: ")
    print(" ")
    typy=set()
    i = 0
    while i < ileLiczb:
        typ=int(input("Give numbers %s: " % (i+1)))
        if typ not in typy:
            typy.add(typ)
            i = i+1
            print("Your numbers: \n", typy)
            print(" ")
    print("\nThe drawn numbers are:", liczby)

    trafione = set(liczby) & typy
    if trafione:
        print("\nNumber of hits: %s" % len(trafione))
        print("\nCongratulations!!! Hit numbers: ", trafione,)
        if len(trafione) == 1:
            print("Your payment: 3$")
        elif len(trafione) == 2:
            print("Your payment: 5$")
        elif len(trafione) == 3:
            print("Your payment: 10$")
        elif len(trafione) == 4:
            print("Your payment: 100$")
        elif len(trafione) == 5:
            print("Your payment: 3500$")
        elif len(trafione) == 6:
            print("WOOOOW! HUUUUUUGE WIN!!!")
            print("!!!!  1 000 000 $ !!!!")
        else:
            print(" 0 ")
    else:
        print("\nSorry! You missed a number :( Good luck next time!")
else:
    print("Ok! See you soon!  :D")
