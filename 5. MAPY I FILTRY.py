#FUNKCJA MAP - SLUZY DO STOSOWANIA FUNKCJI NA KAZDYM ELEMENCIE LISTY

liczby=[i for i in range(1,11)]
parzyste=list(map(lambda x:x*2,liczby)) #ZASADNICZO TO TO SAMO CO
#parzyste=[i*2 for i in liczby]
print(parzyste)
print("\n")

#LAMBDA POZWALA NA DYNAMICZNE PODANIE TRESCI FUNKCJI, KTORA MA BYC WYKONANA
#ZAPIS "X:" OZNACZA ZE DYNAMICZNA FUNKCJA PRZYJMUJE JEDEN PARAMETR
#ZAPIS "X*2" OKRESLA SPOSOB PRZETWORZENIA ELEMENTU WSKAZANEGO PRZEZ PARAMETR

#FUNKCJA FILTER

liczby=[i for i in range(1,21)]
parzyste=list(filter(lambda x: x%2==0, liczby))
#TO SAMO CO parzyste=[x for x in liczy if x%2==0]
print(parzyste)
