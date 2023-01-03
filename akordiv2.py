tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "B"]
ton = 0
count = 0
broj_dozvoljenih_pogresaka = 3
while ton not in tonovi and ton is not 'H':
    ton = input()
    if ton == 'H':
        ton = 'B'
        break
    count+=1
    print("Pogrešan unos")
    if count > broj_dozvoljenih_pogresaka:
        break

index = tonovi.index(ton)
nova_lista = tonovi[index:]
nova_lista.extend(tonovi[:index])
print(nova_lista)
dur_index_drugi = 4
dur_index_treci, mol_index_treci = 7, 7
mol_index_drugi = 3

print(f'{ton} dur se sastoji od tonova {ton} {nova_lista[dur_index_drugi]} {nova_lista[dur_index_treci]}, a mol od {ton} {nova_lista[mol_index_drugi]} {nova_lista[mol_index_treci]}')