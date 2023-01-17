import json
import requests
import os


def provjeri_postoji_li_file(ime_datoteke):
    """Vraća true ako datoteka postoji, ako ne postoji, onda vraća false"""
    return os.path.exists(ime_datoteke)

def procitaj_json_iz_datoteke(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka_koju_citamo:
        procitani_dict = json.load(datoteka_koju_citamo)
        print(procitani_dict)

def upisi_json_iz_datoteke(ime_datoteke, vrijednost_za_upis):
    with open(ime_datoteke, "w", encoding="utf-8") as datoteka_u_koju_pisemo:
        json.dump(vrijednost_za_upis, datoteka_u_koju_pisemo, indent=4)

def dohvati_podatke_s_urla(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        json_s_weba = response.json()
    else:
        json_s_weba = []
        #json_s_weba = {}
    return json_s_weba

def ispisi_dict(dict_s_weba):
    print(json.dumps(dict_s_weba, indent = 4))

URL = "https://jsonplaceholder.typicode.com/posts"

#mozda_dict = dohvati_podatke_s_urla(URL)

#for key, value in mozda_dict.items():
#    print(f"{key} = {value}")

lista_dictova = dohvati_podatke_s_urla(URL)

""" for mozda_dict in lista_dictova[0:5]:
    for key, value in mozda_dict.items():
       print(f"{key} = {value}") """

#for mozda_dict in lista_dictova[0:1]:
#    for key, value in mozda_dict.items():
#       print(f"{key}")

#Zadatak: ispisati podatke za dict koji je na indeksu 2 u lista_dictova
#koristiti ispisi_dict


#ispisi_dict(lista_dictova[2])


#ZADATAK:
#1. dohvatiti listu postova sa  URL-a
#2. ako ne postoji datoteka naziva "post_s_weba.json":
#   dict koji je na indeksu 2 u lista_dictova zapisati u lista_dictova
#3. ako datoteka postoji:
#   pročitati što piše u njoj
#   a dict s weba samo ispisati
ime_datoteke = "post_s_weba.json"

if provjeri_postoji_li_file(ime_datoteke):
    procitaj_json_iz_datoteke(ime_datoteke)
    ispisi_dict(lista_dictova[2])
else:
    upisi_json_iz_datoteke(ime_datoteke, lista_dictova[2])

#4. u funkciji procijat_json_iz_datoteke koristiti funkciju ispisi_dict za ispis umjesto print
#5. ako možete, pokušajte ovo pretvoriti u klasu koja prima dva parametra kod inicijalizacije
#url i ime datoteke
#6. pozivanjem metode dohvati_ili_ispisi(self) neka se dogodi sve iz koraka 1-3