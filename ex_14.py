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