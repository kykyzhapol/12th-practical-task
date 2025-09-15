#1
'''
with open('text.txt', 'r') as f:
    file = f.read()

m_spaces = 0
current = 0

for i in file:
    if i == ' ':
        current += 1
        m_spaces = max(m_spaces, current)
    else:
        current = 0

print(m_spaces)

#2
with open('text.txt', 'r') as f:
    file = f.read()

m_pair = 1
current = 1

for i in range(0, len(file)-1):
    if file[i] == file[i+1]:
        current += 1
        m_pair = max(m_pair, current)
    else:
        current = 0

print(m_pair+1)

#3
with open('text.txt', 'r') as f:
    file = f.read()
list(file)

let = set()
for i in file:
    if ('А' <= i <= 'я') or ('A' <= i <= 'z'):
        let.add(i)
print(len(let))

#4
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()

for i in file:
    if file.count(i) == 3:
        print(i)
        break
print(file.count('а'))

#5
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.readlines()

symbols = set()
for lines in file:
    other_text = file
    other_text.remove(lines)
    for let in lines:
        if let not in other_text[0] and let != '\n':
            symbols.add(let)

print(*symbols)

#6
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

#7
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()
file.reverse()

m_len = 100000
for i in range(0, len(file)):
    while not file[i].isalpha():
        file[i] = file[i][:-1]
    m_len = min(m_len, len(file[i]))

print(file, m_len)
'''
