x=1
while(x<=10):
    print(x)
    x+=1 #ZEBY PETLA BYLA SKONCZONA, INACZEJ X=X+1

print("\n")

for x in range(1,11):
    print(x) #ITERACJA, ZAKRES NIEDOMKNIETY

print("\n")


for x in range(1,11,2):
    print(x) #CO DRUGA WARTOSC

print("\n")


for x in range(10,0,-1):
    print(x) #OD TYLU

print("\n")

#ZAGNIEZDZANIE PETLI

for y in range(1,11):
    for x in range(1,11):
        print('y={}, x={}'.format(y,x))
#NA 1 OBROT PETLI Y PRZYPADA 10 OBROTOW PETLI X

print("\n")

#ZAGNIEZDZENIE PETLI WHILE

y,x=1,1
while(y<=10):
    x=1
    while(x<=10):
        print('y={}, x={}'.format(y,x))
        x+=1
        y+=1

print("\n")

#BREAK

for x in range(1,101):
    if(x%17.5==0):
        print("szukana liczba to {}".format(x))
        break

print("\n")

#CONTINUE

for x in range(-10,11):
    if(x==0):
        continue
    print(1/x) #POJAWI SIE WYJATEK DZIELENIA PRZEZ 0




