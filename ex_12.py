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
