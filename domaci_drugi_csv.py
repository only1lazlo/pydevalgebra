#zadatak 2:
#korištenjem vjezba_pisanje_csv_u_file.py i rješenjem zadatka za čitanje iz CSV filea
#pokušati napuniti dict kako bi dobili iste podatke u dict-u kakve imamo u vjezba_pisanje_csv_u_file.py
#tako da vrijednosti_za_upis bude jednak vrijednosti_za_ispis
import os

def provjeri_postoji_li_file(ime_datoteke):
    """Vraća true ako datoteka postoji, ako ne postoji, onda vraća false"""
    return os.path.exists(ime_datoteke)

ime_datoteke = "vjezba_csv_ban_jelacic.csv"

def procitaj_csv_iz_datoteke(ime_datoteke):
    dict_kojeg_citamo = {}
    with open(ime_datoteke, "r") as datoteka_koju_citamo:
        linije = datoteka_koju_citamo.readlines()
        for linija in linije:
            #print(linija.rstrip())
            #linija je zarezom odvojen niz znakova
            #prvi string prije zareza je kljuc, ostalo je vrijednost
            vrijednosti_linije = linija.rstrip().split(',')
            #print(vrijednosti_linije)
            if len(vrijednosti_linije) == 2:
            #prvi string prije zareza je kljuc
                kljuc = vrijednosti_linije[0]
                dict_kojeg_citamo[kljuc] = vrijednosti_linije[1]
            #problem sa jezicima "['hrvatski'", " 'njemački']"
            if len(vrijednosti_linije) > 2:
            #prvi string prije zareza je kljuc
                kljuc = vrijednosti_linije[0]
                dict_kojeg_citamo[kljuc] = vrijednosti_linije[1:]
            #problem sa jezicima "['hrvatski'", " 'njemački']"
            lista_jezika = []
            for jezik in vrijednosti_linije[1:]:
                #jezik.strip().strip("'[]'") znači
                #.strip() -> miče prvi razmak koji nam smeta
                #.strip("'[]") -> miče ostale znakove koji nam smetaju
                vrijednost_za_u_dict = jezik.strip().strip("'[]")
                lista_jezika.append(vrijednost_za_u_dict)
            dict_kojeg_citamo[kljuc] = lista_jezika
    return dict_kojeg_citamo

if provjeri_postoji_li_file(ime_datoteke):
    dobiveni_dict = procitaj_csv_iz_datoteke(ime_datoteke)
    for key, value in dobiveni_dict.items():
        print(f'{key}: {value}')

else:
    print(f"{ime_datoteke} ne postoji!")