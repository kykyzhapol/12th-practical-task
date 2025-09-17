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