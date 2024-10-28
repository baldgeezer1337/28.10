with open ("dati.txt","r", encoding="utf-8") as file:
    saturs=file.read()
vardi=saturs.split()
unikalie_vardi_skaits=len(set(vardi))

print(saturs)
print(vardi)
print(len(vardi))
print('Unikālo vārdu skaits:',unikalie_vardi_skaits)


with open ("dati.txt","r", encoding="utf-8") as file:
    rindas=file.readlines()

for index,rinda in enumerate(rindas,start=1):
    if rinda.strip():
        print(f"{index}:{rinda.strip()}")


