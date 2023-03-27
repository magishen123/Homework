category = input ('Категория товара:')
wish = input ('Предпочтение: ')

if category == 'молочные продукты':
    if wish == 'фермерское':
        print ('Экоферма')
else:
    print( 'Моё село')

if category == 'хлеб':
    if wish == 'цельнозерновой':
        print('Пекарня дяди Коли')
else:
    print("Хлебзавод №21")