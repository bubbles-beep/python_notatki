#PRZYDATNE TAM, GDZIE BEDZIEMY POTRZEBOWAC KODU WIELOKROTNEGO UZYTKU
#MOGA PRZYJMOWAC PARAMETRY ROZNYCH TYPOW, MOGA ZWRACAC DANE
#NIE MOZE BYC W PLIKU DWOCH FUNKCJI O TEJ SAMEJ NAZWIE, NAWET JESLI
#ROZNIA SIE PARAMETRAMI

#DEKLAROWANIE FUNKCJI

def sayHello():
    print("Hello my friend!")
sayHello()
print("\n")

#DEKLARACJA FUNKCJI MUSI ZNAJDOWAC SIE NAD JEJ WYWOLANIEM
#DLATEGO FUNKCJE DEKLARUJEMY NA POCZATKU PLIKU LUB W OSOBNYM MODULE, KTORY
#IMPORTUJEMY NA POCZATKU PLIKUS

#PARAMETRY FUNKCJI - SLUZA DO PRZEKAZYWANIA DO NIEJ DANYCH

def sayHello2(imie):
    print("Hello my friend {}!".format(imie))
sayHello2("esterka")
print("\n")

def dodaj(x, y):
    print(x+y)

#MOGA PRZYJMOWAC WIELE PARAMETROW, ROZDZIELAMY JE PRZECINKAMI

def sayHello3(imie):
    imie="Czeslaw"
    print("Hello my friend {}!".format(imie))
sayHello3("Czeslaw")
print("\n")

#JAK SPRAWDZIC TYPY DANYCH, KTORE ZOSTALY PODANE PRZEZ PARAMETRY:

def sprawdz_typ(x):
    if(isinstance (x, int)):
        print('otrzymalem liczbe calkowita')
    else:
        print('otrzymalem cos innego')
sprawdz_typ("x")
print("\n")


#DEKLARACJA WARTOSCI DOMYSLNEJ DLA PARAMETRU FUNKCJI

def domyslne_wartosci(a="brak", b="brak"):
    print('a='+a)
    print('b='+b)
#WTEDY MOZEMY (ALE NIE MUSIMY) PODAC WARTOSCI PARAMETROW TEJ FUNKCJI:

domyslne_wartosci ("X", "Y")
domyslne_wartosci () #FUNKCJA PRZYJMUJE WARTOSCI DOMYSLNE
domyslne_wartosci("cos") #MNIEJ WARTOSCI NIZ PARAMETROW - PRZYPISANE SA WG.
#KOLEJNOSCI, A POZOSTALE PRZYJMA WARTOSCI DOMYSLNE
domyslne_wartosci (b="cos innego") #PRZEKAZYWANIE ARTOSCI DO PARAMETROW PO NAZWIE
print("\n")

#ZWRACANIE WYNIKOW Z FUNKCJI
#MOGA TO BYC STRINGI, INT, ZLOZONE STRUKTURY - NP. TABLICE

def oddaj0():
    return 0
print(oddaj0())
print("\n")

#PRZYKLAD ZE ZLOZONYM TYPEM DANYCH

def dajcyferki():
    l=list(range(10))
    return 1
dajcyferki()
print(dajcyferki())
print("\n")

#LAMBDA 

fun=lambda a,b: a+b
print (fun(10,20))
print("\n")

#ZWRACA CIALO FUNKCJI, NIE MOZE BYC TU NP. PRINTA

def nielambda(a,b):
    return a+b
print("\n")


