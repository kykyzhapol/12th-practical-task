#reading file
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

#staying only letters
for i in range(0, len(file)):
    file[i] = file[i].lower()
    while not file[i].isalpha():
        file[i] = file[i][:-1]

fst = file[0]
file = set(file)
file.remove(fst)
print(file)

for i in file:
    if len(set(i)) == len(i):
        print(i)