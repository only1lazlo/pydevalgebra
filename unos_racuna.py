from datetime import datetime
from klasa_racun_domaci import Racun, Stavka
from ..Vjezba002.funkcije import umnozak

def dodaj_stavke(racun):
    """
    racun je tipa Racun, objekt koji smo kreairali tako da smo instancirali klasu Racun
    """
    while True:
        proizvod = input("Unesi ime proizvoda: ")
        cijena = float(input("Unesi cijenu proizvoda: "))
        kolicina = float(input("Unesi kolicinu proizvoda: "))
        
        stavka_2 = Stavka(proizvod, cijena, kolicina)
        racun.dodavanje_stavki(stavka_2)
        izlaz = input("Završen unos stavki? Da/Ne ")
        if izlaz == "Da":
            break

broj_racuna = 1
lista_racuna = []

while True:
    izlaz = input("Završen unos Računa? Da/Ne ")
    if izlaz == "Da":
        break
    datum = datetime.date.today()
    racun = Racun(broj_racuna, datum.strftime("%d.%m.%Y"))
    broj_racuna += 1
    racun.dodaj_stavke()
    lista_racuna.append(racun)

print("Gotov unos")
print("#"*20)

for racun in lista_racuna:
    racun.ispis_racuna()



a = 5
b = 2
umnozak(a, b)