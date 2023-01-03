""" naziv_liste napunit s range 100 brojeva korištenjem for petlje
copy kopirati u nova_lista

broj ponavljanja elementa u novoj listi korištenjem count

string banana for petljom count od element iz banane """

""" naziv_liste = list(range (0, 100, 1))
nova_lista = list()

#nova_lista = naziv_liste.copy()
for element in naziv_liste:
    nova_lista[element]= naziv_liste[element]
    nova_lista.count(element)    

banana = "banana"

for slovo in banana:
    print(banana.count(slovo))

 """


naziv_liste = []
for x in range(0,100,1):
    naziv_liste.append(x)

nova_lista = naziv_liste.copy()



for element in nova_lista:
    print(f'Element {element} se pojavljuje {nova_lista.count(element)} puta u listi')

banana = 'banana'
for slovo in banana:
    print(f'Slovo {slovo} se u \'banana\' pojavljuje {banana.count(slovo)} puta u listi')

