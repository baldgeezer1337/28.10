with open('vardi.txt', 'w', encoding='utf-8') as faila_objekts:
    while True:
        vards=input('Ievadiet vardu (ievadiet "beigt", lai pabeigtu):')
        if vards.lower()=='beigt':
            break
        faila_objekts.write(vards+'\n')


print('\nIevaditie vardi:')
with open('vardi.txt', 'r', encoding='utf-8') as faila_objekts:
    for rinda in faila_objekts:
        print(rinda.strip())