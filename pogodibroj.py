pogodi_me= int(input("Unesi broj od 1 do 100 "))
broj = 50
while broj != pogodi_me:
    if pogodi_me > broj:
        broj+=1
    elif pogodi_me < broj:
        broj-=1




print(f'Bravo, broj je {broj}')


""" broj=0
while broj != pogodi_me:
    broj = int(input("Unesi broj "))
    if pogodi_me > broj:
        print('Broj je veći')
    elif pogodi_me < broj:
        print('Broj je manji')
print(f'Bravo, broj je {broj}')  """


