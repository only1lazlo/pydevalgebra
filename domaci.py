#zadatak 1:
#pokušati umjesto json.loads koristiti json.load -> pogledati dokumentaciju za json modul u Pythonu!
import os
import json

def provjeri_postoji_li_file(ime_datoteke):
    """Vraća true ako datoteka postoji, ako ne postoji, onda vraća false"""
    return os.path.exists(ime_datoteke)

def procitaj_json_iz_datoteke(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka_koju_citamo:
        procitani_dict = json.load(datoteka_koju_citamo)
        print(procitani_dict)

ime_datoteke = "vjezba_json_ban_jelacic.json"

procitaj_json_iz_datoteke(ime_datoteke)

if provjeri_postoji_li_file(ime_datoteke):
    procitaj_json_iz_datoteke(ime_datoteke)

else:
    print(f"{ime_datoteke} ne postoji!")



