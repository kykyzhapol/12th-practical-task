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