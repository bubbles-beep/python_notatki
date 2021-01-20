#FUNKCJA JAKO ARGUMENT

def razy2(a): #TA FUNKCJA JAKO ARGUMENT, PRZYJMUJE LICZBE...
    return a*2 #...KTORA ZWRACA PODWOJONA

def funkcja_jako_argument(f,x):#DOWOLONA FUNKCJA F - BO FUNKCJA PRINT - MUSI BYC
    #ARGUMENT
    print(f(x))#LICZBA KTORA ZOSTANIE PODANA DO FUNKCJI "FUNKCJA_JAKO..."
    
funkcja_jako_argument(razy2,33)
print("\n")

#PRZYKLAD PRZEKAZYWANIA FUNKCJI JAKO ARGUMENT I ARGUMENTOW *ARGS
#KOD POWODUJE WYSWIETLENIE KAZDEJ Z WARTOSCI *ARGS PO OBROBCE FUNKCJA
#PRZEKAZANA JAKO ARGUMENT
#FUNKCJA OBRABIAJACA JEST F. POWIEKSZ, KTORA ZWRACA POWIEKSZONY OTRZYMANY
#PRZEZ ARGUMENT TEKST

def powieksz(x):
    return x.upper()

def zastosuj_dla_wszystkich(fun,*args):
    for a in args:
        print(fun(a))

zastosuj_dla_wszystkich(powieksz,'siala','baba','mak')
print("\n")

#FUNKCJE MOGA BYC PRZEKAZYWANE ROWNIEZ JAKO LISTY
#PRZYKLAD ZASTOSOWANIA RZEDU FUNKCJI NA JEDNEJ ZMIENNEJ

def pomnoz_razy_dwa(x): #DEKLARACJA FUNKCJI
    return x*2

def podziel_przez_trzy(x):
    return x/3

def dodaj_piec(x):
    return x+5

funkcje=[pomnoz_razy_dwa,podziel_przez_trzy,dodaj_piec]
#LISTA REFERENCJI DO OBIEKTOW FUNKCJI

def obrob(wartosc,*funkcs):
     for f in funkcs:
        wartosc=f(wartosc)
     return wartosc

print(obrob(1,pomnoz_razy_dwa,podziel_przez_trzy,dodaj_piec))
print("\n")

#FUNKCJA W FUNKCJI
#WIDZIANA BEDZIE TYLKO W DANEJ FUNKCJI

def zewnetrzna(x):
    def wewnetrzna(x):
        return x*2
    print(wewnetrzna(x))

zewnetrzna(50)
print("\n")

#ZWRACANIE FUNKCJI Z FUNKCJI
#FUNKCJE SA OBIEKTAMI - MOZEMY PRZYJMOWAC JE PRZEZ ARGUMENTY I ZWRACAC

def wybierz(tryb):
    def powieksz(x):
        return x.upper() #DEKLARACJA FUNKCJI - POWIEKSZENIE
    def pomniejsz(x):
        return x.lower() #DEKLARACJA FUNKCJI - POMNIEJSZENIE
    if tryb==1:
        return powieksz
    elif tryb==2:
        return pomniejsz

funkcja=wybierz(1)
print(funkcja('Witaj swiecie!'))
funkcja=wybierz(2)
print(funkcja('Witaj swiecie!'))
print("\n")
#W ZALEZNOSCI OD LICZBY, KTORA PODAMY JAKO ARGUMENT (1 CZY 2),
#ZOSTANIE ZWROCONA JEDNA ALBO DRUGA FUNKCJA
#PRZY WYWOLANIU ODBIERAMY ZWRACANA FUNKCJE I STOSUJEMY WOBEC TEKSTU

#INNY PRZYKLAD:

def daj_funkcje(x):
    def podwoj(a):
        return a*2
    def polowa(a):
        return a/2
    if x==1:
        return podwoj
    elif x==2:
        return polowa

fun=daj_funkcje(1)
print (fun(6))
print("\n")

#ZAPIS "return podwoj" A NIE "return podwoj()", BO ZWRACAMY OBIEKT FUNKCJI
#DRUGI ZAPIS ZWRACA WYNIK JEJ DZIALANIA PO WYWOLANIU

#REKURENCJA
#CZYLI WYWOLANIE FUNKCJI PRZEZ SAMA SIEBIE, AZ DO UZYSKANIA OKRESLONEGO WYNIKU
#PRZYKLAD Z SILNIA:

def silniaRek(n):
    if n==0:
        return 1
    else:
        return n*silniaRek(n-1)

#INNY PRZYKLAD

def rekurencyjny_wypisywacz(n):
    print(n)
    if n>0:
        rekurencyjny_wypisywacz(n-1)
    else:
        return n
    return n
rekurencyjny_wypisywacz(10)






