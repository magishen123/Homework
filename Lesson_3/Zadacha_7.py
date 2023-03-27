category = input('введите категорию товара - ')
category = category.lower()

if category == 'продукты':
    summa = int(input('-'))
    if summa <= 100:
        print('Попробуйте нашу выпечку')
    elif summa > 100 and summa <= 500:
        print ('Как на счет орехов в шоколаде')
    else:
        print('Попробуйте экзотические фрукты')
else:
    print('Загляните в товары для дома')