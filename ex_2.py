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