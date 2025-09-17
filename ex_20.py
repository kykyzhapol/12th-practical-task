num = input()

num_l = []
for unit in num:
    try:
        num_l.append(int(unit))
    except:
        #ignore non number simbols
        continue


def first(x):
    '''function for converting in russian first unit'''
    match int(x):
        case 1:
            return 'один'
        case 2:
            return 'два'
        case 3:
            return 'три'
        case 4:
            return 'четыре'
        case 5:
            return 'пять'
        case 6:
            return 'шесть'
        case 7:
            return 'семь'
        case 8:
            return 'восемь'
        case 9:
            return 'девять'
        case _:
            return ''


def ten(x):
    '''function for converting in russian ten's'''
    match int(x):
        case 11:
            return 'одинадцать'
        case 12:
            return 'двенадцать'
        case 13:
            return 'тринадцать'
        case 14:
            return 'четырнадцать'
        case 15:
            return 'пятнадцать'
        case 16:
            return 'шетнадцать'
        case 17:
            return 'семьнадцать'
        case 18:
            return 'восемьнадцать'
        case 19:
            return 'девятнадцать'
        case _:
            return ''


def second(x):
    '''function for converting in russian second unit'''
    match int(x):
        case 2:
            return 'двадцать'
        case 3:
            return 'тридцать'
        case 4:
            return 'сорок'
        case 5:
            return 'пятьдесят'
        case 6:
            return 'шестьдесят'
        case 7:
            return 'семьдесят'
        case 8:
            return 'восемьдесят'
        case 9:
            return 'девяносто'
        case _:
            return ''


def third(x):
    '''function for converting in russian third unit'''
    match int(x):
        case 1:
            return 'сто'
        case 2:
            return 'двести'
        case 3:
            return 'триста'
        case 4:
            return 'четыреста'
        case 5:
            return 'пятьсот'
        case 6:
            return 'шестьсот'
        case 7:
            return 'семьсот'
        case 8:
            return 'восемьсот'
        case 9:
            return 'девятьсот'
        case _:
            return ''


#adding zeros in the beginning of list if numbers
while len(num_l) < 9:
    num_l.insert(0, 0)

millions = num_l[:3]
thousands = num_l[3:6]
units = num_l[6:9]

millions_str = str()
thousands_str = str()
units_str = str()

if millions != [0, 0, 0]:
    if millions[1] == 1:
        tens = int(str(f'{millions[1]}{millions[2]}'))
        millions_str = f'{third(millions[0])} {ten(tens)} миллионов'
    else:
        declension = str()
        if millions[2] == 1:
            declension = 'миллион'
        elif 1 < millions[2] < 5:
            declension = 'миллиона'
        else:
            declension = 'миллионов'
        millions_str = f'{third(millions[0])} {second(millions[1])} {first(millions[2])} {declension}'

if thousands != [0, 0, 0]:
    if thousands[1] == 1:
        tens = int(str(f'{thousands[1]}{thousands[2]}'))
        thousands_str = f'{third(thousands[0])} {ten(tens)} тысяч'
    else:
        declension = str()
        if millions[2] == 1:
            declension = 'тысяча'
        elif 1 < millions[2] < 5:
            declension = 'тысячи'
        else:
            declension = 'тысяч'
        thousands_str = f'{third(thousands[0])} {second(thousands[1])} {first(thousands[2])} {declension}'

if units != [0, 0, 0]:
    if units[1] == 1:
        tens = int(str(f'{units[1]}{units[2]}'))
        units_str = f'{third(units[0])} {ten(tens)}'
    else:
        units_str = f'{third(units[0])} {second(units[1])} {first(units[2])}'

print(millions_str, thousands_str, units_str)