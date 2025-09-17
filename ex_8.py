with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

for i in range(0, len(file)):
    file[i] = file[i].lower()
    while not file[i].isalpha():
        file[i] = file[i][:-1]

file.sort(key=len)
print(*file)