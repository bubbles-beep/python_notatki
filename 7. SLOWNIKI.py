#SLOWNIK TO ZBIOR SKLADAJACY SIE Z KLUCZA I WARTOSCI POWIAZANEJ Z TYM KLUCZEM
#SA MODYFIKOWALNE

#TWORZENIE SLOWNIKOW

slownik=()
slownik2=dict()

info={"LG" : "telewizorek przyjazny rodzinie",
         "SONY" : "japonska technologia",
         "SAMSUNG" : "idz pan"}

#POBIERANIE WARTOSCI ZE SLOWNIKOW

print(info["LG"])

#ITERACJA

for i in info:
    print(info[i])
print("\n")

for k in info.keys():
    print(info[k]) #TO SAMO CO WYZEJ
print("\n")

#FUNKCJA VALUES - ZAMIAST KLUCZY ZWRACA LISTE WARTOSCI

print(info.keys())
print("\n")

print(info.values())
print("\n")

#SPRAWDZAMY CZY OBIEKT ZNAJDUJE SIE NA LISCIE

if "LG" in info:
    print("mamy taki produkt")
else:
    print("nie mamy")
print("\n")

if "idz pan" in info.values(): #SZUKANIE PO VALUES
    print("mamy")
else:
    print("nie mamy")
print("\n")

#MODYFIKACJA ZAWARTOSCI

info["KLUCZ"]="WARTOSC" #DODANIE I NADPISANIE
del info["LG"] #KASOWANIE ELEMENTU

print("\n")



