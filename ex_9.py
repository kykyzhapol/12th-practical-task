with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

for i in range(0, len(file)):
    file[i] = file[i].lower()
    while not file[i].isalpha():
        file[i] = file[i][:-1]

for comp in file:
    file_an = file
    file_an.remove(comp)
    for comper in file:
        if comp == comper:
            print(comp)
            break