""" lista = range(1,31,1)

for i in lista:
    if i % 3 == 0:
        print(f'i{i} je djeljiv s 3')
    if i % 6 == 0:
        print(f'i{i} je djeljiv s 6')
    if i % 9 == 0:
        print(f'i{i} je djeljiv s 9')
    else:
        print() """


rijec = input("Unesi palindrom: ")

obrnuta_rijec = rijec[::-1]
""" #prvi nacin
obrnuta_rijec = rijec[::-1]

if rijec == obrnuta_rijec:
    print(f'Riječ "{rijec}" je palindrom')
else:
    print(f'Riječ "{rijec}" nije palindrom') """

#drugi nacin
lista_1 = []
obrnuta_lista = []

for slovo in rijec:
    lista_1.append(slovo)

obrnuta_lista = list(reversed(lista_1))

if rijec == obrnuta_rijec:
    print(f'Riječ "{rijec}" je palindrom')
else:
    print(f'Riječ "{rijec}" nije palindrom')

