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
        
        

    def ispis_racuna(self):
        print(f'Broj računa: {self.broj_racuna}')
        print(f'Datum izdavanja: {self.datum_izdavanja}')
        print()
        print("Stavke računa: ")

        print('\tProizvod\t\tCijena\t\tKolicina')
        print('-'*50)
        for stavka in self.stavke:
            print(stavka)
        print('-'*50)
        self.ukupni_iznos()
        self.iznos_pdv()
        print(f"Ukupni iznos: {self.ukupan_iznos} EUR")
        print(f'Ukupni iznos s PDV-om je: {self.ukupan_iznos + self.pdvcijena}')

    #DODAVANJE STAVKI
    def dodavanje_stavki(self, proizvod, cijena, kolicina):
        self.stavke.append({"proizvod":proizvod, "cijena": cijena, "kolicina": kolicina})
    
    #IZRACUN PDV-A
    def iznos_pdv(self):
        self.pdvcijena = 0
        for stavka in self.stavke:
            self.pdvcijena += stavka["cijena"]*0.25
        print(f'Iznos PDV-a je: {self.pdvcijena}')

    #IZRACUN UKUPNOG IZNOSA
    def ukupni_iznos(self):
        self.ukupan_iznos = 0
        for stavka in self.stavke:
            self.ukupan_iznos += stavka["cijena"]

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
racun_2.dodavanje_stavki("Sir", 2.5, 1)
racun_2.ispis_racuna()




