
while True: 
      ievade = input('Ievadiet yes or no: ')
      if ievade =='yes':
        n = input("Ievadiet grānatas nosaukumu: ")
        a = input("Ievadiet autoru: ")
        gads = int(input("Ievadiet gadu: "))
        book_inf = (f'Nosaukums: {n}\n Autors: {a}\n Gads: {gads}')
      else:
            break 

with open("book.txt", "w", encoding="utf-8") as faila_objekts:
        for file in book_inf:
              faila_objekts.write(file)