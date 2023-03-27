per = input('game = ')

if per == 'game':
    print('Игра - угадай число')

    for y in range(3):
        i = input('Продолжить игру - ')
        if i == 'нет':
            break
        elif i = 'да':
            for i in range(3):
                num = int(input('введите число'))
                if num == 5:
                    print('You win ticket on ball')
                    break
                else:
                    print('Good luck next time')
        else:
            print('Игра окончена - введено не правильное значение')
print('Игра окончена')