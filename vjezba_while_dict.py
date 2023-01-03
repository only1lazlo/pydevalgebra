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

broj_keyeva_u_dictu = len(vozni_park)

key = 1

while key < broj_keyeva_u_dictu:
    print(key, end='\n\t')
    brojac_elemenata = 0
    while brojac_elemenata < len(vozni_park[key]):
        print(vozni_park[key][brojac_elemenata], end='\n\t')
        brojac_elemenata += 1
    print()
    key += 1

for key in vozni_park.keys():
    print()