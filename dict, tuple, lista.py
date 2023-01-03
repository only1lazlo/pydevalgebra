ulazni_podaci = [
    ('Pero', 'Developer'),
    ('Ante', 'Developer')
]

moj_dict = {}

for i in ulazni_podaci:
    prvi_kljuc = None
    for j in i:
        if i.index(j) == 0:
            moj_dict[j] = ""
            prvi_kljuc = j
        else:
            moj_dict[prvi_kljuc] = j 
'''
prvi_kljuc = None
for element in ulazni_podaci:
    for i in element:
        if element.index(i) == 0:
            moj_dict[i] =""
            prvi_kljuc = i
        else:
            moj_dict[prvi_kljuc] = i
        '''
#for i, j in ulazni_podaci:
  #  moj_dict[i] = j

print(moj_dict.items())
    
       
   # moj_dict = {ulazni_podaci[i]}
