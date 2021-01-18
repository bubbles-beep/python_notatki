#WYJATKI

#print(1/0)
#print("dalej") #DRUGA LINIJKA NIE ZOSTALA WYPISANA, BO PROGRAM ZOSTAL PRZERWANY
#W MOMENCIE POJAWIENIA SIE WYJATKU

#TRY-EXCEPT-FINALLY-ELSE


try:
    print(1/0)
except:
    print("nie poszlo")
print("dalej")
print("\n")
#GDYBY PO INSTRUKCJI print(1/0) ZNALAZLY SIE KOLEJNE, NIE ZOSTALYBY WYKONANE

try:
    print(1/0)
except ZeroDivisionError:
    print("nie mozna dzielic przez zero")
print("\n")
#OBSLUZYLISMY TYLKO WYJATEK DZIELENIA PRZEZ ZERO

try:
    print(1/0)
except ZeroDivisionError:
    print("nie mozna dzielic przez zero")
except:
    print("jakis inny blad")
print("\n")
#GDYBY KOD SPOWODOWAL POJAWIENIE SIE INNEGO BLEDU

#WYJATKI MOZNA OBSLUZYC ZBIORCZO:
try:
    print(1/0)
except(ZeroDivisionError, IOError):
    print("albo to, albo to")
print("\n")

#ODEBRANIE KOMUNIKATU BLEDU - NP. ZEBY ZAREJESTROWAC GO W LOGACH
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
print("\n")

#WYKONANIE CZYNNOSCI NIEZALEZNIE OD WYSTAPIENIA LUB NIE WYJATKU
try:
    print(1/0)
except:
    print("wyjatek")
finally:
    print("i tak dziala")
print("\n")

#ZAREAGOWANIE, KIEDY WYJATEK NIE WYSTAPI:
try:
    print("info")
except ValueError:
    print("wyjatek")
else:
    print("nie bylo wyjatku")
print("\n")

#WYWOLANIE WYJATKU, NAWET JESLI NIE WYSTAPIL
try:
    raise TypeError()
except TypeError:
    print("tak mialo byc")
