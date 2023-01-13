try:
    #int("1")
    #r znači read
    #w znači write
    #a -> ako postoji nastavi pisanje (append), a ako ne postoji kreiraj i počni pisati
    #rb -> b znači binary format

    datoteka_koju_citamo = open("pero.txt", "r") #open vraća varijablu
    print(datoteka_koju_citamo.readlines())

except ValueError as e:
    print(e)

else:
    print("Sve je u redu")

finally:
    print("Ovo se uvijek izvršava")
    datoteka_koju_citamo.close()

#novi način, bolji lakši
koliko_je_uspjelo = 0
for ime_datoteke in ["ante.txt", "pero.txt"]:  #nije case sensitive, NEMOJ STAVLJATI RAZMAKE U IME DATOTEKE
    try:
        with open(ime_datoteke, "r") as datoteka_koju_citamo:
            print(f"{ime_datoteke} ima sadržaj: ")
            linije = datoteka_koju_citamo.readlines()
            for linija in linije:
                print(linija.rstrip())
                # ako koristimo ovo ispisat će i prazan redak između
                #print(linija)
            koliko_je_uspjelo += 1

    except FileNotFoundError as err:
        print(err)
        #tu šaljemo poruke o grešci

    finally:
        print(f"opet smo gotovi, {koliko_je_uspjelo} datoteka smo uspješno obradili")
        #a tu da smo gotovi UVIJEK!

