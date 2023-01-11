from datetime import datetime
import locale

""" print(datetime.date.today().strftime("%d.%m.%Y"))
print(datetime.datetime.now().strftime("%d.%m.%Y. %H:%M:%S"))
print(datetime.datetime.now().isoformat())

 """

locale.setlocale(locale.LC_ALL, "hr_Hr")

"""a, b, c = input("unesi datum kao DD.MM.YYYY").split(".")
print(a, b, c)
print(datetime.date(int(a), int(b), int(c)))

def funkcija(a = datetime.date):
    print(a.strftime("%A"))

funkcija(datetime.date((int(a), int(b), int(c)))) """

def ispisi_dan_u_tjednu(datum):
    print(datum.strftime("%A"))

unos = input("Unesi datum u obliku YYYY-MM-DD ")

datum_korisnika = datetime.strptime(unos, "%Y-%m-%d")
ispisi_dan_u_tjednu(datum_korisnika)