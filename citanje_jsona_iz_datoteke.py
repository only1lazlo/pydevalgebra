import json

ime_datoteke = "vjezba_json_ban_jelacic.json"


print(f"{ime_datoteke} ima sadržaj: ")

with open(ime_datoteke, "r") as datoteka_koju_citamo:
    linije = datoteka_koju_citamo.readlines()
    for linija in linije:
        print(linija.rstrip())
        dict_linija = json.loads(linija)                #load strings
        print(dict_linija['jezici'])            #printaj samo ključ jezici
        
        for i in dict_linija:               #printa vrijednosti iz ključeva
            print(dict_linija[i])
