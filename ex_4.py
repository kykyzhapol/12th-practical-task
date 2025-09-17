with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()

for i in file:
    if file.count(i) == 3:
        print(i)
        break
print(file.count('а'))