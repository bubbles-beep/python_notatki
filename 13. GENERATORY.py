#GENERATOR TO FUNKCJA, KTORA MOZE ZOSTAC WSTRZYMANA I WZNOWIONA OD
#MIEJSCA, W KTORYM ZOSTALA WSTRZYMANA CECHUJA SIE "LENIWA" EWALUACJA
#TWORZA KOLEJNE ELEMENTY DOPIERO W MOMENCIE ODWOLANIA SIE DO GENERATORA
#POZWALA TO NA WYDAJNIEJSZE WYKORZYSTANIE PAMIECI OPERACYJNEJ ORAZ
#ZWROCENIE NIESKONCZONEJ ILOSCI ELEMENTOW W PAMIECI PRZECHOWYWANY JEST
#TYLKO JEDEN AKTUALNIE POBIERANY ELEMENT, A NIE CALA LISTA

for x in range(10):
    print(x)
#KONSTRUKCJA TA POZWALA NA ITEROWANIE PO KOLEJNYCH ELEMENTACH ZWRACANYCH
#PRZEZ RANGE
    print("\n")

def elementy():
    yield 'element nr 1'
    yield 'element nr 2'
    yield 'element nr 3'
    yield 'element nr 4'

for e in elementy ():
    print(e)

#FUNKCJA 'ELEMENTY' ZA POMOCA SLOWA KLUCZOWEGO 'YIELD' PODAJE NAM
#KOLEJNE ELEMENTY. 'YIELD' ODPOWIADA ZA PRZERWANIE WYKONANIA FUNKCJI,
#ZAPISANIE JEGO AKTUALNEGO STANU I ZWROCENIE KOLEJNEJ WARTOSCI
#We should use yield when we want to iterate over a sequence but don’t want to
#store the entire sequence in memory.

print("\n")

#ADAPTACJA RANGE PODAJACA WARTOSCI CO 10:

def myrange(n):
    for x in range(n):
        yield x*10

for x in myrange(10):
    print(x)

print("\n")

#PODANIE TYLE POTEG KOLEJNYCH LICZB, ILE GENERATOR OTRZYMA PRZEZ ARGUMENT:

def potegi2(n):
    for x in range(1, n+1):
        yield pow(2,x)

for p in potegi2(5):
    print(p)

print("\n")

#FUNKCJA GENERUJACA, KTORA BEDZIE NAM ZWRACALA KOLEJNE DZIESIECI:

def dziesieci():
    i=1
    while True:
        yield i*10
        i+=1

dz=dziesieci()
print(next(dz))
print(next(dz))
print(next(dz))

print("\n")

#GENERATOR MOZE ODDAWAC WARTOSCI ROZNYCH TYPOW I GENEROWAC JE NA ROZNE
#SPOSOBY, WAZNE BY ODDAWAC KOLEJNE WARTOSCI ZA POMOCA 'YIELD':

def poryRoku():
    pory=['wiosna','lato','jesien','zima']
    for e in pory:
        yield e

for p in poryRoku():
    print(p)

print("\n")

#INNY PRZYKLAD:

def parzyste(n):
    for x in range(n+1):
        yield 2*x

for p in parzyste(10):
    print(p)

print("\n")
    
#KORZYSTANIE Z PLIKU .CSV
#import csv
#with open('imiona.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)


def rozbijacz_csv(np,r):
    import csv
    with open(np, 'r') as plik:
        while True:
            linia=plik.readline()
            print(linia)
            if not linia:
                break
                yield linia.strip().split(r)
rc=rozbijacz_csv('imiona.csv',';')
print(rc)
