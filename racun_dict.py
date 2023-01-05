def dodaj_racun(redni_broj):    
    broj_racuna = f'BR-2023-01-{redni_broj}'
    datum_izdavanja = '05.01.2023.'
    stavke = [
    {
        "proizvod": "Mlijeko",
        "cijena": 2.0,
        "kolicina" : 5
    },
    {
        "proizvod": "Kruh",
        "cijena" : 2.0,
        "kolicina" : 5
    }
    ]
    iznos_pdv = 0
    ukupan_iznos = 0

    for stavka in stavke:
        ukupan_iznos += stavka["cijena"]

    iznos_pdv = ukupan_iznos*0.25

    racuni.append({
        "broj_racuna": broj_racuna,
        "datum_izdavanja": datum_izdavanja,
        "stavke": stavke,
        "iznos_pdv": iznos_pdv,
        "ukupan_iznos" : ukupan_iznos

    })

racuni = []
def ispisi_racune():
    for racun in racuni:
        print()
        print(f'Broj računa: {racun["broj_racuna"]}')
        print(f'Datum izdavanja: {racun["datum_izdavanja"]}')

        print(f'Stavke računa:')

        print('\tProizvod\t\tCijena\t\tKolicina')
        print('-'*50)
        for stavka in racun["stavke"]:
            print(f'\t{stavka["proizvod"]}\t\t\t{stavka["cijena"]}\t\t{stavka["kolicina"]}')

        print()
        print(f'Ukupan iznos računa: {racun["ukupan_iznos"]}')
        print(f'Iznos PDV: {racun["iznos_pdv"]}')
        print()


dodaj_racun(1)
dodaj_racun(2)
dodaj_racun(3)
ispisi_racune()
