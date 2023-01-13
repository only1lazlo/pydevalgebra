#novi način, bolji lakši
koliko_je_uspjelo = 0
for ime_datoteke in ["pero_pisanje.txt"]:  #nije case sensitive, NEMOJ STAVLJATI RAZMAKE U IME DATOTEKE
    try:
        #with open(ime_datoteke, "w") as datoteka_u_koju_pisemo:      #ovo zamjenjuje tekst svaki put
        with open(ime_datoteke, "a") as datoteka_u_koju_pisemo:  #ovo nadodaje tekst na postojeći
            print(f"{ime_datoteke} punimo sadržaj: ")
            for linija in range(1, 3):
                string_koji_ide_u_datoteku = f"Pero je super {linija}\n"
                datoteka_u_koju_pisemo.write(string_koji_ide_u_datoteku)
                koliko_je_uspjelo += 1

    except FileNotFoundError as err:
        print(err)
        #tu šaljemo poruke o grešci

    finally:
        print(f"opet smo gotovi, {koliko_je_uspjelo} datoteka smo uspješno obradili")
        #a tu da smo gotovi UVIJEK!