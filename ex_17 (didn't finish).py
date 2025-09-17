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

mat_symb = ['+', '-', '*', '/', '^']


#calculating
#for i in exp:

#    print(numexpr.evaluate(i).item())