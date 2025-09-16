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

#8
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

for i in range(0, len(file)):
    file[i] = file[i].lower()
    while not file[i].isalpha():
        file[i] = file[i][:-1]

file.sort(key=len)
print(*file)

#9
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

for i in range(0, len(file)):
    file[i] = file[i].lower()
    while not file[i].isalpha():
        file[i] = file[i][:-1]

for comp in file:
    file_an = file
    file_an.remove(comp)
    for comper in file:
        if comp == comper:
            print(comp)
            break

#10
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

#11
#Petya - first, Vasya  - second

with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()
file = file.split()

for i in range(0, len(file)):
    file[i] = file[i].lower()

for city_ix in range(0, len(file)-1):
    if file[city_ix][-1] != file[city_ix+1][0]:
        if city_ix % 2 == 1:
            print('Vasya win')
            break
        else:
            print('Petya win')
            break
    if city_ix+2 == len(file):
        if city_ix % 2 == 1:
            print('Petya win')
        else:
            print('Vasya win')

#12
import keyword

kw = keyword.kwlist

name = input('Enter name of value -->')
error_count = 0

if name in kw:
    error_count +=1
    print('er1')
if name[0].isdigit():
    error_count +=1
    print('er2')
for let in name:
    if 'A' <= let <= 'z' or let == '_' or name.isalnum():
        pass
    else:
        error_count += 1
        print('er3')

match error_count:
    case 0:
        print('available name')
    case _:
        print('name in not available')

#13
def lucky_check(x):

    if len(x)%2 == 0:
        if sum(int(digit) for digit in x[len(x)//2:]) == sum(int(digit) for digit in x[:len(x)//2]):
            return True
    return False

tickets = False
cnt = 0
while tickets == False:
    cnt+=1
    tickets = lucky_check(input('enter your ticket number -->'))
print(cnt)

#14
clue = input('подсказка -->')
word = input('слово -->')
word_list = [i for i in word]
guess_list = ['*']*len(word)
try_q = 25
print('\n'*25, clue)
while try_q > 0:
    try_q -=1
    print(*guess_list)
    cho =  int(input('Буква или слово (0 - буква, 1 - слово)?'))
    match cho:
        case 1:
            guess_word = input('Слово?')
            if guess_word == word:
                print('Победа!')
                break
            else:
                print('Проигрыш!')
                break
        case 0:
            let = input('Буква?')
            if let in word_list:
                for i in range(len(word_list)):
                    if let == word_list[i]:
                        guess_list[i] = let
            else:
                print('Нет такой буквы')
else:
    print('Вы проиграли')

#15

num = 1
while len(str(num)) != 4 or len(set(str(num))) != 4:
    try:
        num = int(input('Введите 4х значное целое число с различными цифрами -->'))
    except:
        continue
print('\n'*25)

#Быки - цифры совпавшие с загаданным числом и при этом находящиеся на тех же позициях.
#Коровы - цифры, которые есть в загаданном числе, но находятся на других позициях
num_l = [int(i) for i in str(num)]
try_q = 10
bools = 0
cows = 0
while try_q>0 and bools!=4:
    bools, cows = 0, 0
    try_q -= 1
    num_g = [int(i) for i in input()]
    for n in range(len(num_l)):
        if num_l[n] == num_g[n]:
            bools +=1
        if num_g[n] in num_l:
            cows +=1
    print(f'Быков: {bools}, Коров: {cows-bools}')

#16
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
'''
#17
import re
import numexpr


#reading files
with open('text.txt', 'r', encoding='UTF-8') as f:
    file = f.read()

#searching ()
file_lst = [i for i in file]
position1, position2 = [], []
for i in range(len(file_lst)):
    if file_lst[i] == ')':
        position2.append(i)
    if file_lst[i] == '(':
        position1.append(i)

#create new list and added there expression inside brackets
exp = []

for i in range(len(position2)):
    exp.append(file[position1[-1-i]+1:position2[i]])

#add rest in list (not in the brackets)
exp.append(f'{file[:position1[0]]}{file[position2[-1]:]}')


#delite multiple occurrences
for cl in range(len(exp)):
    exp[cl] = re.sub(r'\([^)]*\)', '', exp[cl])
print(exp)

#delite last trash
for cl in range(len(exp)):
    exp[cl] = re.sub(r'[()]', '', exp[cl])
print(exp)




#calculating
for i in exp:

    print(numexpr.evaluate(i).item())
