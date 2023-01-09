class Stavka:
    def __init__(self, proizvod, cijena, kolicina):
        self.proizvod = proizvod
        self.cijena = cijena
        self.kolicina = kolicina
    
    def iznos(self):
        return self.cijena*self.kolicina
    
    def ispis(self):
        print(f'\t{self.proizvod}\t\t\t{self.cijena}\t\t{self.kolicina}')

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
        self.stavke = []
        #ako je korisnik unio stavke, uzmi tu vrijednost
        if stavke:
            for stavka in stavke:
                self.dodavanje_stavki(stavka)

        self.ukupan_iznos = 0
        self.pdvcijena = 0
        

    def ispis_racuna(self):
        print(f'Broj računa: {self.broj_racuna}')
        print(f'Datum izdavanja: {self.datum_izdavanja}')
        print()
        print("Stavke računa: ")

        print('\tProizvod\t\tCijena\t\tKolicina')
        print('-'*50)
        for stavka in self.stavke:
            stavka.ispis()

        print('-'*50)
        self.ukupni_iznos()
        self.iznos_pdv()
        print(f"Ukupni iznos: {self.ukupan_iznos} EUR")
        print(f'Ukupni iznos s PDV-om je: {self.ukupan_iznos + self.pdvcijena} EUR')

    #DODAVANJE STAVKI
    def dodavanje_stavki(self, stavka):
        self.stavke.append(stavka)
    
    #IZRACUN PDV-A
    def iznos_pdv(self):
        self.pdvcijena = 0
        for stavka in self.stavke:
            self.pdvcijena += stavka.iznos()*0.25
        print(f'Iznos PDV-a je: {self.pdvcijena}')

    #IZRACUN UKUPNOG IZNOSA
    def ukupni_iznos(self):
        self.ukupan_iznos = 0
        for stavka in self.stavke:
            self.ukupan_iznos += stavka.iznos()

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
stavka = Stavka("Mlijeko", 1.75, 2)

#racun = Racun(1, '05.01.2023.', 
      #  stavke=[])
#racun.ispis_racuna()

racun_2 = Racun(2, '04.01.2023.')

while True:
    proizvod = input("Unesi ime proizvoda: ")
    cijena = float(input("Unesi cijenu proizvoda: "))
    kolicina = float(input("Unesi kolicinu proizvoda: "))
    stavka_2 = Stavka(proizvod, cijena, kolicina)
    racun_2.dodavanje_stavki(stavka_2)
    izlaz = input("Završen unos stavki? Da/Ne ")
    if izlaz == "Da":
        break
#racun_2.dodavanje_stavki(stavka)
racun_2.ispis_racuna()

#ZADATAK:
#1. NAPRAVITI FUNKCIJU KOJA DODAJE STAVKE U PROIZVOD (GORNJU WHILE PETLJU PRETVORITI U FUNKCIJU)
#2. OMOGUĆITI DODAVANJE VIŠE RAČUNA U KOJE MOEMO DODAVATI STAVKE KORIŠTENJEM FUNKCIJE IZ ZADATKA POD 1.
#       a. svaki račun mora imati jedinstven broj računa!!
#3. KOD ORGANIZIRATI:
#   - KREIRATI FOLDER Racuni
#   -unutar tog foldera kreirati praznu datoteku naziva __init__.py
#   -unutar tog istog foldera uz __init__.py kreirati datoteku racun.py u kojoj cete napisati rjesenje