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