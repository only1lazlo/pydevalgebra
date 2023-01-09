class Osoba:

    def __init__(self, ime, prezime, oib):
        self.ime = ime
        self.prezime = prezime
        self.oib = oib

    def ispis(self):
        print(f'{self.ime}, {self.prezime}')
        print(f'OIB: {self.oib}')
        print()

pero = Osoba("Pero", "Perić", "12345678911")
#pero.ispis()

class Zaposlenik(Osoba):
    def __init__(self, ime, prezime, oib, ime_tvrtke):
        super().__init__(ime, prezime, oib)
        self.ime_tvrtke = ime_tvrtke

    """ def ispis(self):
        #ovaj ispis zamijenjuje ispis klase Osoba
        print(f'{self.ime}, {self.prezime}')
        print(f'OIB: {self.oib}')
        print(f'Zaposlen u {self.ime_tvrtke}')
        print() """
    #ovako se to radi s super
    def ispis(self):
        super().ispis()
        print(f'Zaposlen u {self.ime_tvrtke}')

stipe = Zaposlenik("Stipe", "Stipić", "12345678912", "Kamenolom d.o.o.")
#stipe.ispis()

class Penzic(Osoba):
    #def __init__(self, ime, prezime, oib):
     #   super().__init__(ime, prezime, oib)

    def ispis_penzije(self):
        print("Penzija je mala, moraš natrag na posao")

artur = Penzic("Artur", "macak", None)
artur.ispis()
artur.ispis_penzije()
