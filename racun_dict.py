class Racun:
    """Ova klasa definira sve potrebno kako bi radili s računom"""
    def __init__(self, broj_racuna, datum_izdavanja, stavke=None):
        """
        broj_racuna i datum_izdavanja su OBAVEZNI ARGUMENTI
        stavke su OPCIONALNI ARGUMENT
        ako se ne pošalju, bit će prazna lista
        None je defaultna vrijednost
        kao defaultne vrijednosti UVIJEK koristiti nepromijenjive vrijednosti
        """

        self.broj_racuna = broj_racuna
        self.datum_izdavanja = datum_izdavanja
        #ako je korisnik unio stavke, uzmi tu vrijednost
        if stavke:
            self.stavke = stavke
        else:
            #inače nemamo stavke, odnosno
            self.stavke = []
        self.iznos_pdv = 0.0
        self.ukupan_iznos = 0.0
        

    def ispis_racuna(self):
        print(f'Broj računa: {self.broj_racuna}')
        print(f'Datum izdavanja: {self.datum_izdavanja}')
        print()
        print("Stavke računa: ")

        print('\tProizvod\t\tCijena\t\tKolicina')
        print('-'*50)
        for stavka in self.stavke:
            print(stavka)
        print()

    def dodavanje_stavki(self, ime, br_cijena, br_kolicina):
        self.stavke.append({"proizvod":ime, "cijena":br_cijena, "kolicina": br_kolicina})


    #ZADATAK: napisati metodu u klasi Račun za dodavanje stavke
    #pretpostavke: stavka se sastoji od imena proizvoda i cijene
    #stavku spremiti u listu stavki (self.stavke) kao što smo to radili u prethodnom primjeru

    #PRIMJER nakon dodavanja dvije stavke: 
    """ stavke=[
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
    """

racun = Racun(1, '05.01.2023.', 
        stavke=[{"proizvod": "Mlijeko",
        "cijena": 2.0,
        "kolicina" : 5
        }])
racun.ispis_racuna()

racun_2 = Racun(2, '04.01.2023.')
racun_2.dodavanje_stavki("Sir", 5.50, 1)
racun_2.ispis_racuna()
