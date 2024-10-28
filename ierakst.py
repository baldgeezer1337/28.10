datiti=[ 'pirmais', 'otrais', 'trešais']
with open('datiti.txt', 'w', encoding='utf-8') as faila_objekts:
    for ieraksts in datiti:
        faila_objekts.write(ieraksts + '\n')