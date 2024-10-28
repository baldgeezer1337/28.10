'''with open ("dati.txt","r", encoding="utf-8") as file:
    saturs=file.read()

print(saturs)
with open ("dati.txt","r", encoding="utf-8") as file:
    rindas=file.readlines()

print(rindas)

for rinda in rindas:
    print(rinda.strip())

with open ("dati.txt","r", encoding="utf-8") as file:
  for rinda in file:
    print(rinda.strip())'''


noraiditais_burts='f'
with open('teksts.txt', 'r', encoding='utf-8') as file:
    saturs=file.read()
saturs=saturs.lower()
vardi=saturs.split()
saraksts=[ ]

for elements in vardi:
    if elements[0]==noraiditais_burts:
        saraksts.append(elements[0])
        len(elements)>0 and elements[0]==noraiditais_burts
    print(elements[0])

print(saraksts)
print(saturs)
print(vardi)
print(len(saraksts))