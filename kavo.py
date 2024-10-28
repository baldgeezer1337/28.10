datititi=input('Ievadiet savu vardu: ')
with open('datititi.txt', 'w', encoding='utf-8') as faila_objekts:
    for ieraksts in datititi:
        faila_objekts.write(ieraksts)