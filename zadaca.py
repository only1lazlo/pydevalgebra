#NAPOMENA: JAVLJA SE GREŠKA PRI UNOSU POLOGA ODNOSNO PODIZANJA NOVCA UKOLIKO SE NE UNESE FLOAT VRIJEDNOST, ODNOSNO BROJ SA TOČKOM - BUDE SE ISPRAVILO
def izbornik():
    izbor = -1
    while izbor != 0 or 1 or 2 or 3 or 4 or 5:      #petlja za izbornik
        
        print("""Izaberite opciju:
    1 - Otvaranje računa tvrtke
    2 - Prikaz stanja računa
    3 - Prikaz prometa po računu
    4 - Polog novca na račun
    5 - Podizanje novca s računa
    0 - Izlaz iz programa
    """)
        izbor = int(input())
    
        if izbor == 1:
            print("Izabrali ste otvaranje računa tvrtke")
            return Otvaranje_racuna()

        elif izbor == 2:
            print("Izabrali ste prikaz stanja računa")
            return Prikaz_stanja_racuna()

        elif izbor == 3:
            print("Izabrali ste Prikaz prometa po računu")
            return Prikaz_prometa()

        elif izbor == 4:
            print("Izabrali ste Polog novca na račun")
            return Polog_novca()

        elif izbor == 5:
            print("Izabrali ste Podizanje novca s računa")
            return Podizanje_novca()

        elif izbor == 0:
            exit()

import random                   #za dodjeljivanje userID

Popis_racuna = {}               #dict u kojeg se spremaju svi podaci
Ime_tvrtke = ""                 
Adresa_tvrtke = ""
Promet = []
Stanje_racuna = 0



def Otvaranje_racuna():                                 #NAPOMENA, MORAM DORADITI PETLJU UKOLIKO RANDOM KREIRA VEĆ POSTOJEĆI USERID - male su šanse za to, ali može se dogoditi
    random_broj = random.randint(000000, 999999)        #za stvaranje userID koji se koristi kao ključ u dictu

    Ime_tvrtke = input("Unesite ime Vaše tvrtke: ")

    Adresa_tvrtke = input("Unesite adresu Vaše tvrtke: ")

    if random_broj not in Popis_racuna:                                                 #ako userID postoji pokreni ponovno funkciju   - MORA SE DORADITI
        dict1 = {random_broj:[Ime_tvrtke, Adresa_tvrtke, Stanje_racuna, Promet]}
        Popis_racuna.update(dict1)

    print(f"Vaš jedinstveni ID je {random_broj}, nemojte ga izgubiti")
    print()

    return izbornik()


def Prikaz_stanja_racuna():

    Izbor_korisnika = int(input("Unesite svoj ID: "))

    if Izbor_korisnika in Popis_racuna:
        print(f'Stanje Vašeg računa je: {Popis_racuna[Izbor_korisnika][2]}')
        print()
    else:
        print(f"Korisnik {Izbor_korisnika} ne postoji!")

    return izbornik()


def Prikaz_prometa():

    Izbor_korisnika = int(input("Unesite svoj ID: "))

    if Izbor_korisnika in Popis_racuna:
        print(f"Prikaz prometa: \n{Popis_racuna[Izbor_korisnika][3]}")

        
    else:
        print(f"Korisnik {Izbor_korisnika} ne postoji!")

    return izbornik()

def Polog_novca():
#TODO: zapisati vrijeme
    Izbor_korisnika = int(input("Unesite svoj ID: "))

    if Izbor_korisnika in Popis_racuna:
        Polog = float(input("Unesite koliko novca želite položiti na svoj račun: "))
        round(Polog, 2) #možda treba promijeniti

        Popis_racuna[Izbor_korisnika][2] += Polog
        Popis_racuna[Izbor_korisnika][3].append(str('+' + str(Polog)))

        print(f"Dodali ste {Polog} na svoj račun")
        print()
    else:
        print(f"Korisnik {Izbor_korisnika} ne postoji!")

    return izbornik()

def Podizanje_novca():
#TODO: zapisati vrijeme
    Izbor_korisnika = int(input("Unesite svoj ID: "))

    if Izbor_korisnika in Popis_racuna:
        Podizanje = float(input("Unesite koliko novca želite podići sa svog računa: "))
        round(Podizanje, 2) #možda treba promijeniti

        if Podizanje > Popis_racuna[Izbor_korisnika][2]:
            print("Nemate dovoljno sredstva za podići taj iznos")
            print()
        
        else:
            Popis_racuna[Izbor_korisnika][2] -= Podizanje
            Popis_racuna[Izbor_korisnika][3].append(str('-' + str(Podizanje)))
            print(f"Podigli ste {Podizanje} sa svog računa")
            print()

    else:
        print(f"Korisnik {Izbor_korisnika} ne postoji!")
    return izbornik()
izbornik()