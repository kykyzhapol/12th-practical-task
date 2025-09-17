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