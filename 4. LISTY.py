#TWORZENIE LIST

lista=[]
lista2=list() #OBIE LISTY SA TAKIE SAME (PUSTE)

lista3=[1,2,3,"kotek"]
print(lista3)

print("\n")

lista4=["nie","toperz",123,lista3] #ELEMENTEM MOZE BYC INNA LISTA
print(lista4)

print("\n")

#POBIERANIE WARTOSCI Z LIST

print(lista4[1]) #POBIERAMY ELEMENT
print("\n")

print(lista4[-2]) #OD KONCA
print("\n")

print(lista4[1:3]) #ELEMENT DRUGI I TRZECI
print("\n")

print(lista4[1:-1]) #ELEMENT OD DRUGIEGO DO PRZEDOSTATNIEGO LUB:
print(lista4[1:len(lista4)-1])
print("\n")

print(lista4[:3]) #POBRANIE DO POZYCJI 3 WLACZNIE
print("\n")

print(lista4[2:]) #POBRANIE DO TRZECIEJ POZYCJI
print("\n")

print(lista4[:]) #WYSWIETLENIE CALEJ LISTY
print("\n")


#ITEROWANIE PO LISTACH
li=["siala","baba","mak","az","dalo","jej","sie","w","znak","po","100","kroc"]
for l in li:
    print(l)
print("\n")


#SPRAWDZENIE CZY ELEMENT JEST NA LISCIE

poszukiwane=["szczescie","milosc","pieniadze","piwo"]
if("piwo" in poszukiwane):
    print("no nie wiem")
else:
    print("tak jest")

print("\n")

#MODYFIKOWANIE ZAWARTOSCI LISTY:

#DODAWANIE DO LISTY

lista=[1,2,3,4,5,6,7]
lista.append(8) #DODAJE NA KONCU LISTY
print(lista)
print("\n")

lista.insert(0,"X") #PODSTAWIA WARTOSC W MIEJSCE WSKAZANEGO INDEKSU, PRZESUWA
#RESZTE ELEMENTOW W PRAWO
print (lista)
print("\n")

lista[2]="Y" #PODMIENIA ELEMENT POD WSKAZANYM INDEKSEM
print(lista)
print("\n")



#KASOWANIE Z LISTY

lista=[1,2,3,0,5,6,2,9]
del lista[2] #SKASOWANIE ELEMENTU O PODANYM INDEKSIE
print(lista)
print("\n")

lista.remove(2) #USUNIE PIERWSZE WYSTAPIENIE WARTOSCI 2 Z LISTY
print(lista)
print("\n")

del lista[0:4] #SKASUJE ELEMENTY O INDEKSACH 0-3
print(lista)
print("\n")

lista.clear() #KASUJE CALA ZAWARTOSC
print(lista)
print("\n")



#SORTOWANIE I ODWRACANIE LIST

lista=["kotek", "piesek", "myszka"]
lista.sort() #SORTUJE ALFABETYCZNIE
print(lista)
print("\n")

lista.sort()
lista.reverse() #SORTUJE ALFABETYCZNIE MALEJACO
print(lista)
print("\n")

lista.sort(reverse=True) #TO SAMO CO WYZEJ
print(lista)
print("\n")


#LISTY Z ELEMENTAMI ROZNYCH TYPOW

lista=[[2,"buk"],[1,"jodla"],[3,"jablon"]]
lista.sort() #SORTUJE PO PIERWSZEJ WARTOSCI Z KAZDEJ Z LIST
print(lista)
print("\n")

from operator import itemgetter 
lista=[[2,"buk"],[1,"jodla"],[3,"jablon"]]
lista.sort(key=itemgetter(1)) #SORTUJE PO INDEKSIE ELEMENTU PODLISTY - TUTAJ
#ALFABETYCZNIE
print(lista)
print("\n")

lista=[1,2,3,5,1,1,10,"batman"]
print(len(lista)) #ILOSC ELEMENTOW W LISCIE
print(lista.count(1)) #ILE RAZY DANY ELEMENT WYSTEPUJE W LISCIE
podlista=lista[2:7] #SKOPIOWANIE DANYCH Z DANEGO ZAKRESU
print(podlista)
kopia=lista.copy() #ABY MODYFIKACJE NA KOPII NIE MODYFIKOWALY ORYGINALNEJ LISTY
print(kopia)
print("\n")


#FUNKCJE AGREGUJACE
list=[1,3,6,8,55,23]
print(sum(list), max(list), min(list))
#SUMA, MAKSYMALNA WARTOSC, MINIMALNA WARTOSC
print("\n")

list=[3,6,5,2,22,33]
print(list.index(33)) #POD JAKIM INDEKSEM ZNAJDUJE SIE WSKAZANY ELEMENT

print("\n")


#LISTY SKLADANE

liczby=[]
for x in range(1,21): liczby.append(x)
print(liczby)
print("\n")

parzyste=[]
for i in liczby:
    if(i%2==0):
        parzyste.append(i)
print(parzyste)
print("\n")

parzyste=[i for i in liczby if i%2==0]
print(parzyste)
print("\n")

#NAJPROSCIEJ

print([i for i in range(1,21) if i%2==0])

