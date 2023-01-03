import random
from turtle import goto


    
def kamen_skare_papir():
    lista=["Kamen", "Škare", "Papir"]
    tvoj_izbor= int(input("Izaberi 0 za kamen, 1 za škare, 2 za papir "))
    if (tvoj_izbor!= 0 or 1 or 2):
        print("Ne zajebavaj")
    odgovor=random.randint(0,2)

    if tvoj_izbor == odgovor:
        print(f"Izabrao si  {lista[tvoj_izbor]}   Protivnik je izabrao   {lista[odgovor]}  Tie!")

    elif tvoj_izbor == 0 and odgovor == 1 or tvoj_izbor==1 and odgovor==2 or tvoj_izbor ==2 and odgovor==0:
        print(f"Izabrao si  {lista[tvoj_izbor]}   Protivnik je izabrao {lista[odgovor]}  Win!")

    elif tvoj_izbor == 0 and odgovor == 2 or tvoj_izbor== 1 and odgovor==0 or tvoj_izbor == 2 and odgovor==1:
        print(f"Izabrao si  {lista[tvoj_izbor]}   Protivnik je izabrao  {lista[odgovor]}  Lose!")
while True:
    kamen_skare_papir()