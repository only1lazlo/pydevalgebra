vozni_park = {
    1:['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00 ],
    2:['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00 ],
    3:['Tegljač', 'MAN', 'RI 001 ZZ', 2019, 78000.00 ],
    4:['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00 ],
    5:['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00 ],
    6:['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00 ],
    7:['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00 ],
    8:['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00 ],

}
kljuc_tip = 'tip'
kljuc_proizvodjac = 'proizvođač'
kljuc_registracija = 'registarska oznaka'
kljuc_godina_registracije = 'prva godina registracije'
kljuc_cijena_u_eurima = 'Cijena u EUR'

vozni_park_sa_dict_u_value = {}

for kljuc, vrijednost in vozni_park.items():
    nova_vrijednost_dict = {
        kljuc_tip : vrijednost[0],
        kljuc_proizvodjac : vrijednost[1],
        kljuc_registracija: vrijednost[2],
        kljuc_godina_registracije: vrijednost[3],
        kljuc_cijena_u_eurima : vrijednost[4]
    }
    vozni_park_sa_dict_u_value = nova_vrijednost_dict
for k, v in vozni_park_sa_dict_u_value.items():
    print(f'k={k}, v={v}')
print()


