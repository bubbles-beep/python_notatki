#DEKORATOR TO STRUKTURALNY WZORZEC OBIEKTOWY POZWALA NA DYNAMICZNE
#DODANIE NOWEJ FUNKCJONALNOSCI DO ISTNIEJACEJ KLASY PODCZAS DZIALANIA
#PROGRAMU
#ZASADA DZIALANIA POLEGA NA OPAKOWANIU ORYGINALNEJ KLASY TZW KLASA DEKORUJACA
#PAMIETAJ:
#FUNKCJA MOZE BYC PRZEKAZYWANA DO INNEJ FUNKCJI JAKO PARAMETR
#FUNKCJA MOZE BYC DEFINIOWANA WEWNATRZ INNEJ FUNKCJI
#FUNKCJA MOZE ZWRACAC INNA FUNKCJE

#PRZYPOMNIENIE:
#FUNKCJA JAKO ARGUMENT

def obrob(fun,a,b):
    print(fun(a,b))

def dodaj(a,b):
    return a+b

def odejmij(a,b):
    return a-b

obrob(dodaj,10,5)
obrob(odejmij,10,5)
print("\n")

#FUNKCJA W FUNKCJI

def zewnetrzna():
    def wewnetrzna(a,b):
        return a*b
    x=wewnetrzna(4,5)
    return x

print(zewnetrzna())
print("\n")

#ZWRACANIE FUNKCJI Z FUNKCJI
def zewnetrzna():
    def wewnetrzna(a,b):
        return a*b
    return wewnetrzna
x=zewnetrzna()
print(x(19,3))
print("\n")

#TWORZENIE DEKORATOROW

#DEKORATOR TO FUNKCJA, KTORA PRZYJMIE PRZEZ ARGUMENT DEKOROWANA FUNKCJE,
#TWORZY WEWNETRZNA FUNKCJE, KTORA NADPISUJE DZIALANIE FUNKCJI
#DEKOROWANEJ, A NASTEPNIE ZWRACA FUNKCJE WEWNETRZNA

def doopakowania():
    print('do opakowania')

def dekorator(fun):
    def opakowujaca():
        print('opakowujaca')
        fun()
    return opakowujaca

dek=dekorator(doopakowania)
dek()

print("\n")

#INNY PRZYKLAD:

def dekorator(fun):
    def wewnetrzna():
        print('jakies dodatkowe dzialania')
        fun()
    return wewnetrzna

@dekorator #TO CO PO "@" TO NAZWA FUNKCJI DEKORUJACEJ
def funkcja():
    print('jestem funkcja')

funkcja()
print("\n")

#DEKOROWANIE FUNKCJI Z PARAMETRAMI
#MOZEMY POSLUZYC SIE *args LUB **kwargs

def dekorowana(x):
    print(f'siema {x}')

def dekorator(fun):
    def wewn(x):
        print('przed')
        fun(x)
        print('po')
    return wewn

d=dekorator(dekorowana)
d('Andrzej')
print("\n")

#ALTERNATYWNA TECHNIKA DAJACA TEN SAM WYNIK DZIALANIA:

def dekorator(fun):
    def wewn(x):
        print('przed')
        fun(x)
        print('po')
    return wewn

@dekorator
def dekorowana(x):
    print(f'siema {x}')

dekorowana('Andrzej')
print("\n")

#DRUGI WARIANT PRZEKAZWYWANIA ARGUMENTOW
#PAMIETAJ: *args I *kwargs MAJA BYC PODANE PO FUNKCJI

def funkcja(imie):
    print(f'hello {imie}!')

def dekorator(fun,*args):
    def wewn():
        print('dekoracja')
        fun(*args)
    return wewn

f=dekorator(funkcja,'Andrzej')
f()
print("\n")

#ALTERNATYWNY SPOSOB TWORZENIA DEKORATORA:

def dekorator(fun,*args):
    def wewn(*args):
        print('dekoracja')
        fun(*args)
    return wewn

@dekorator
def funkcja(imie):
    print(f'hello {imie}!')
print("\n")

#DOKUMENTOWANIE FUNKCJI
#SPROWADZA SIE TO DO UMIESZCZENIA TEKSTU POMIEDZY ZNACZNIKAMI """)

def zdokumentacja():
    """to jest dokumentacja tej funkcji"""
    pass
help(zdokumentacja)



