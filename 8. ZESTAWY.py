#ZESTAWY TO ZBIORY ELEMENTOW BEZ POWTORZEN, ZADNA WARTOSC NIE MOZE SIE POWTORZYC
#UZYTECZNE NP. DO USUWANIA DUPLIKATOW
#AUTOMATYCZNIE SIE SORTUJA

#TWORZENIE ZESTAWOW I KONWERSJE Z INNYCH TYPOW ZLOZONYCH
#W ZESTAWACH UZYWAMY {}

z={}
z2=set()
z3={1,2,3,3,5,1}
print(z3)
print("\n")

z4={(1,"a"), (2,"b"), (1,"c"), (1,"a")}
print(z4)
print("\n")
#ZA DUPLIKAT UZNANO KROTKI, KTORE MAJA TA SAMA ZAWARTOSC WSZYSTCKICH ELEMENTOW


lista=[1,2,3,4,3,2,1]
zestaw=set(lista)
lista2=list(zestaw)
print(lista2)
print("\n")
#POZBYLISMY SIE DUPLIKATOW ZE ZBIORU LISTY/KROTKI

#MODYFIKOWANIE ZAWARTOSCI ZESTAWOW: add, remove i clear 

s={1,2,3,4}
s.add(5)
s.remove(1)
print(s)
s.clear()
print("\n")

