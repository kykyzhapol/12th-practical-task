with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file_lst = [i for i in file]
position1, position2 = [], []
for i in range(len(file_lst)):
    if file_lst[i] == ')':
        position1.append(i)
    if file_lst[i] == '(':
        position2.append(i)
print(position2, position1)

if len(position1) == len(position2) and sum(position1) > sum(position2):
    print('all correct')
else:
    print('not all correct')