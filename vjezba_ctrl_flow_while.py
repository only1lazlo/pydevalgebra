#PUNJENJE
brojevi = []

for broj in range(1, 21):
    brojevi.append(broj)

brojevi_za_while = []


brojac = 1

while brojac < 21:
    brojevi_za_while.append(brojac)
    brojac += 1

#ISPIS
for broj in brojevi:
    print(broj, end= ' ')

print()


brojac = 0
while brojac < len(brojevi_za_while):
    print(brojevi_za_while[brojac], end= ' ')
    brojac+=1

