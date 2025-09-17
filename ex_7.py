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