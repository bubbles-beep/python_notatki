#UPPER

napis="siala baba mak"
print(napis.upper())

print("\n")

#LOWER
napis="SIALA BABA MAK"
print(napis.lower())

print("\n")

#TITLE
napis="siala baba mak"
print(napis.title())

print("\n")

#REPLACE)
napis="siala baba mak"
print(napis.replace("a","b"))

print("\n")

#LEN - ILOSC ZNAKOW ZAWARTYCH W CIAGU
x=len("SIALA BABA MAK")
print(x)

print("\n")

#COUNT
napis="siala baba mak na wznak"
print(napis.count("baba")) #FUNKCJA ZWRACA UWAGE NA WIELKOSC LITER

print("\n")

#STRIP - USUWANIE BIALYCH\WSKAZANYCH ZNAKOW LUB CIAGOW

napis="               siala baba mak   "
print(napis.strip())

print("\n")

napis="siala baba mak"
print(napis.strip("mak"))

print("\n")

#SPLIT I JOIN - DZIELENIE LANCUCHA TEKSTOWEGO I ZWRACANIE POD POSTACIA LISTY
#WYRAZOW

napis="siala baba mak"
print(napis.split())

print("\n")

#ITEROWANIE
napis="siala baba mak siala baba mak siala baba mak"
for n in napis:
    print(n)

print("\n")

#MNOZENIE TEKSTU
kriszna= "rama "*5+" "+5*"hare "
print(kriszna)

print("\n")

#SPRAWDZENIE CZY TEKST ZAWIERA DANA FRAZE
if("X" in "SpaceX"):
    print("tak")

print("\n")

#CIECIE LANCUCHOW TEKSTOWYCH

lancuch="123456789"
print(lancuch[2]) #POBRANIE POJEDYNCZEGO ZNAKU ZE WSKAZANEJ POZYCJI
print(lancuch[-2]) #OD KONCA
print(lancuch[2:5]) #OD POZYCJI DO POZYCJI - ZBIOR NIEDOMKNIETY PAMIETAJ
print(lancuch[:5]) #POCZATEK LANCUCHA DO POZYCJI 5 BEZ NIEJ SAMEJ
print(lancuch[:-3])#WW. OD KONCA
print(lancuch[0:6:2]) #CO DRUGI ZNAK OD PIERWSZEJ DO SIODMEJ POZYCJI
print(lancuch[::2]) #WYCIECIE Z CALEGO TEKSTU CO DRUGIEGO ZNAKU


