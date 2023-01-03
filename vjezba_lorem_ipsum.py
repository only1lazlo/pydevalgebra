tekst = ('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard '
'dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. '
'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was '
'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
'publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

count = 0
trazena_rijec = ''
lista_rijeci = tekst.split(' ')

for rijec in lista_rijeci:
    ociscena_rijec = rijec.replace('.', '').replace(',', '').replace('?', '')
    if ociscena_rijec == trazena_rijec:
        count += 1

print(f'Riječ {trazena_rijec} se pojavljuje {count} puta.')