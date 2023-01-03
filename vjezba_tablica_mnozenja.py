while True:

    kraj_tablice = int(input('Unesi do kuda tablica '))
    print('*\t', end ='')
    for i in range (1, kraj_tablice+1):
        print(i, end = '\t')
    
 
    for i in range (1, kraj_tablice+1):
        print()
        print(f'{i}', end ='\t')
        #for j in range (1, kraj_tablice+1):
         #   print(f'{i*j}', end = '\t')
        broj = 1
        while broj < kraj_tablice+1:
            print(f'{i*broj}', end = '\t')
            broj +=1
    print()
    end_program = input("Ako zelis prekinuti program, upisi 1, inace upisi bilo koji drugi broj: ")
    if end_program == '1':
        break

    