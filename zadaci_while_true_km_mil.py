
KOEF_KM = 0.62137119
KOEF_MIL = 1.609344
def konverzija_km_mil():
    while True:
        izbor = input("""Izaberi: 
        1- km u mil ili 
        2- mil u km: """)
        
        if (izbor == "1"):
            unos = float(input("Unesi km "))
            print(f'{unos}km = {unos*KOEF_KM} mil')
    
        elif(izbor == "2"):
            unos = float(input("Unesi mil "))
            print(f'{unos}mil = {unos*KOEF_MIL} km')
    
        else:
            print("Pero ne zajebavaj")

        end_program = input("Ako zelis prekinuti program, upisi 1, inace upisi bilo koji drugi broj: ")
        if end_program == '1':
            break

konverzija_km_mil()