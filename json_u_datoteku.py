import json

vrijednosti_za_upis = {

    "ime" : "Josip",
    "godina" : 1801,
    "jezici" : [
        "hrvatski",
        "njemački"
        ]
    }

ime_datoteke = "vjezba_json_ban_jelacic.json"

with open(ime_datoteke, "w") as datoteka_u_koju_pisemo:  #ovo nadodaje tekst na postojeći
    print(f"{ime_datoteke} punimo sadržaj: ")
    string_koji_cemo_upisati = json.dumps(vrijednosti_za_upis)
    print(string_koji_cemo_upisati)
    datoteka_u_koju_pisemo.write(string_koji_cemo_upisati)

ime_datoteke = "vjezba_json_ban_jelacic_2.json"

with open(ime_datoteke, "w") as datoteka_u_koju_pisemo:  #ovo nadodaje tekst na postojeći
    json.dump(vrijednosti_za_upis, datoteka_u_koju_pisemo, indent=4)