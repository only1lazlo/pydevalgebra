""" prvi_rjecnik = {'auto':'Ford', 'pas':'Airdale', 'boja':'crvena'}
drugi_rjecnik = dict(kuca='dvokatnica', voce='jabuka', povrce = 'mrkva)

print(prvi_rjecnik) """

rjecnik = {
    "voce": ["banana", "jabuka"],
    "povrce":["kupus", "mrkva"],
    1:"auto",
    (4, 5):101
}

print(rjecnik)
print(rjecnik["voce"])
print(rjecnik["povrce"])

voce = rjecnik["voce"]
print(voce[0])
print(rjecnik['voce'][0])

""" for key, value in rjecnik.items():
    print(f'ključ \"{key}" sadrži vrijednost {value}') """

rjecnik_2 ={}
for kljuc, vrijednost in [("pero", "ante"), (1, 101), ("pero", "Stipe")]:
    rjecnik_2[kljuc] = vrijednost
print(rjecnik_2)

