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

#HEADER TABLE ROW
header_top_line = 'ID\tTip\t\tProizvođač\tRegistarska\t\tGodina prve\tCijena'
header_bottom_line = '  \t   \t\t         \toznaka\t\t\tregistracije\t(EUR)'
header_under_line = '_' * 105
print(header_top_line, '\n', header_bottom_line, '\n', header_under_line) 

#BODY TABLE ROWs
for kljuc, vrijednost in vozni_park.items():
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        if type(element) == str:
            if len(element) > 9:
                print(f'{element}', end='\t')
            else:
                print(f'{element}', end='\t\t')
        else:
                print(f'{element}', end='\t\t')
    print() 