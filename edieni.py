edieni=[ 'makaroni', 'kartupelis', 'zupa']
with open('edieni.txt', 'w', encoding='utf-8') as faila_objekts:
    for ieraksts in edieni:
        faila_objekts.write(ieraksts + '\n')