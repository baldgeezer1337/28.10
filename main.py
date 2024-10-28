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


noraiditais_burts='k'
with open('teksts.txt', 'r', encoding='utf-8') as file:
    saturs=file.read()
    saturs=saturs.lower()
    vardi=saturs.split()