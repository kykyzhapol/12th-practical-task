#Petya - first, Vasya  - second

with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

for i in range(0, len(file)):
    file[i] = file[i].lower()

for city_ix in range(0, len(file)-1):
    if file[city_ix][-1] != file[city_ix+1][0]:
        if city_ix % 2 == 1:
            print('Vasya win')
            break
        else:
            print('Petya win')
            break
    if city_ix+2 == len(file):
        if city_ix % 2 == 1:
            print('Petya win')
        else:
            print('Vasya win')