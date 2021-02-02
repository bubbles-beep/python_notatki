#*args

#WYRAZENIA Z JEDNA * UZYWAMY GDY DO FUNKCJI CHCEMY PRZEKAZAC DOWOLNA LICZBE
#ARGUMENTOW POZYCYJNYCH

def args(*args):
    for a in args:
        print(f'{a}')
#DLA KAZDEGO ELEMENTU W "ARGS" WYPISUJEMY JEGO WARTOSC
#ZATEM ARGS JEST ITEROWALNE
args(1,2,3,4,5) #WYWOLANIE FUNKCJI
#ELEMENTY ZOSTALY PRZEKAZANE JAKO LISTA, NIE JAKO KOLEJNE ARGUMENTY!
#DEKLARUJAC ARGUMENT PISZEMY "*", ITERUJAC GO JUZ NIE

print("\n")

def powiekszacz(*slowa):
    for s in slowa:
        print(s.upper())

powiekszacz('siema','tu','mapet',)

#NAZWA *args NIE JEST WYMAGANA, TYLKO PRZYJETA JAKO KONWENCJA, WAZNA JEST "*"

print("\n")

#MOZEMY PRZEKAZAC DODATKOWE PARAMETRY, ALE MUSZA BYC WYMIENIONE JAKO PIERWSZE

def dlakazdego(param1,*args):
    print(f'param1={param1}')
    for a in args:
        print(a)

dlakazdego('pierwsza wartosc','pierwszy arg','drugi arg',3)

print("\n")

#TRZEBA BYC OSTROZNYM PRZY PRZEKAZYWANIU LIST DO TAKIEJ FUNKCJI

def argi(*args):
    for e in args:
        print(e)

argi([1,2,3,4],'cos')

#JEZELI CHCEMY ZEBY KAZDY Z ELEMENTOW BYL POTRAKTOWANY JAKO OSOBNY ARGUMENT,
#MUSIMY LISTE ROZPAKOWAC ZA POMOCA OPERATORA "*"

#argi(*[1,2,3,4,'cos)

print("\n")

#**kwargs

#WYRAZENIA Z "**" STOSUJEMY GDY DO FUNKCJI CHCEMY PRZEKAZAC ZESTAW ARGUMENTOW
#KLUCZ WARTOSC
#W PRZECIWIENSTWIE DO *args ARGUMENTOM PRZYPISZEMY NAZWY, KTORE
#STANA SIE KLUCZEM DLA WARTOSCI
#PO TAK PRZEKAZANYCH ARGUMENTACH PORUSZAMY SIE JAK PO SLOWNIKU

def parametr_kwargs(**kwargs):
    for k in kwargs:
        print(k,kwargs[k])

parametr_kwargs(dodatkowy=48,nastepny=11)
print("\n")

#"k" STANOWI TUTAJ KLUCZ

def kwargs(**parametry):
    print(parametry)

kwargs(param1=1,param2=2,param3=3)
print("\n")

#JESLI CHCEMY DO FUNKCJI PRZEKAZAC PARAMETRY INNE NIZ **kwargs,
#MUSIMY WYMIENIC JE JAKO PIERWSZE (JAK PRZY *args)

def kwargs_argument(argument,**kwargs):
    print(argument)
    print(kwargs)

kwargs_argument(argument=10,param1='andrzej',param2='wiesio')
print("\n")

#PRZYKLAD Z FORMATEM PLIKU csv:

def zapisz_parametry_do_pliku(nazwa_pliku,**parametry):
    plik=open(nazwa_pliku,mode='w',encoding='utf-8')
    for p in parametry:
        plik.write(f'{p};{parametry[p]}\n')
    plik.close()

zapisz_parametry_do_pliku('mojplik.csv',parametr1='wartosc 1',parametr2=2)
print("\n")

#CACHE - OPTYMALIZUJE FUNKCJE

from datetime import datetime
import time

def czekacz():
    time.sleep(1)
    return 1

poczatek=datetime.now()
for x in range(10):
    czekacz()
koniec=datetime.now()
print(koniec-poczatek)

#FUNKCJA "czekacz", KTOREJ ZADANIEM JEST POCZEKANIE 1 SEKUNDY I ZWROCENIE LICZBY
#WYKONYWANA JEST 10-CIOKROTNIE
#NA KONIEC WYPISYWANY JEST CZAS REALIZACJI CALOSCI
#KOD WYKONUJE SIE NIECO PONAD 10 SEKUND
print("\n")

from datetime import datetime
import time
import functools
@functools.lru_cache(maxsize=None)
def czekacz():
    time.sleep(1)
    return 1

poczatek=datetime.now()
for x in range(10):
    czekacz()
koniec=datetime.now()
print(koniec-poczatek)
#FUNKCJA "functools" I DEKORATOR "lru_cache" DZIALANIE JEST SZYBSZE
#maxsize=None OKRESLA DLA ILU WARTOSCI WEJSCIOWYCH FUNKCJA MA PRZYWOLAC CACHE

#CACHE MOZNA STOSOWAC TYLKO DO FUNKCJI DETERMISTYCZNYCH
#CZYLI TAKICH DLA KTORYCH TE SAME WARTOSCI PARAMETROW WEJSCIOWYCH
#ZWROCA NAM ZAWSZE TE SAME DANE

