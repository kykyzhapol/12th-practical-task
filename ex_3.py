with open('text.txt', 'r') as f:
    file = f.read()
list(file)

let = set()
for i in file:
    if ('А' <= i <= 'я') or ('A' <= i <= 'z'):
        let.add(i)
print(len(let))