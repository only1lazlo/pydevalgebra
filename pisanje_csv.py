vrijednosti_za_upis = {

    "ime" : "Josip",
    "godina" : 1801,
    "jezici" : [
        "hrvatski",
        "njemački"
        ]
    }


ime_datoteke = "vjezba_csv_ban_jelacic.csv"

with open(ime_datoteke, "w") as datoteka_u_koju_pisemo:
    print(f"{ime_datoteke} punimo sadržaj: ")
    for key, value in vrijednosti_za_upis.items():
        string_koji_cemo_upisati = f'{key},{value}\n'
        print(string_koji_cemo_upisati)
        datoteka_u_koju_pisemo.write(string_koji_cemo_upisati)

#ZADATAK: napisati u novom modulu  (to će reći novi py file)
#kod koji će pročitati i ispisati linije koje smo dodali u ovom modulu
#iz datoteke u koju smo tu pisali