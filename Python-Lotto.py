import random
print ("..:::PYTHON-LOTTO:::..")
print ("Hi! Do you wanna play Lotto?")
print (" ")
print ("Pick:")
print ("1. YES! LETS'GO")
print ("2. Sorry :( I can't now maybe later.")

answer = input("What is your choice: ")

if answer == '1':
    ileliczb=6
    maksLiczba=49

    liczby = []
    i=0
    while i < ileliczb:
        liczba=random.randint(1,maksLiczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i=i+1
    print ("Wylosowane:", liczby)

else:
    print("Ok! See you soon!  :D")


