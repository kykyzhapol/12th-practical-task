with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()
file.reverse()
for i in range(0, len(file)):
    if file[i][-1] == '.':
        file[i] = file[i][:-1]
    if file[i][-1] == ',':
        file[i] = file[i][:-1]
        file[i-1] = f'{file[i-1]},'
file[-1] = f'{file[-1].lower()}.'
file[0] = file[0].title()

print(*file)