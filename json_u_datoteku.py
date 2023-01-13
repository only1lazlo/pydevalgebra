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
    datoteka_u_koju_pisemo.write(json.dumps(vrijednosti_za_upis))

