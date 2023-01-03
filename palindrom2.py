def palindrom(rijec):

    if rijec.lower() == rijec[::-1].lower():
        return True
    else:
        return False

while True:
   print(palindrom(input("Upiši riječ za koju misliš da je palindrom: ")))