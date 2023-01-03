'''ime = input("Unesi ime ")
prezime = input("Unesi prezime ")
ime_i_prezime = "Ime i prezime je: {} {}".format(ime, prezime)
print(ime_i_prezime)'''

'''ime = input("Unesi ime ")
prezime = input("Unesi prezime ")
ime_i_prezime = f"Ime i prezime je: {ime} {prezime}"
print(ime_i_prezime)'''

'''ime = "Vatroslav"
prezime = "Veble"
god_rodjenja = 1991
drzava_rodjenja = "Hrvatska"
status_radnog_odnosa = "Zaposlen"

tekst = f"Ime je: \"{ime}\"\nPrezime je: \"{prezime}\"\nRođen: {god_rodjenja}.\nDržava rođenja: {drzava_rodjenja}\nZaposlen? {status_radnog_odnosa}"
print(tekst)'''

'''decimalni_broj= 157.3664423
decimalno= f"na 4 decimale je {decimalni_broj:.4f}"
print(decimalno)'''


'''for element in kolekcija:
        instrukcije nad element'''

'''lista_1 = range(1,255, 1)'''
'''lista_1 = [1,2,3,4]
for i in lista_1:
    print(f"{i}", end=" ")'''

"""range(5, 10, 2) = (od, do, koraci)"""
zbroj = 0
for i in range(0,4,1):
    zbroj+=i
    
print(zbroj)