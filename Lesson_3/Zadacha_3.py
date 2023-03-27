category = input ('Категория товара: ')
wish = input ( 'Предпочтение: ')

if category == 'молочные продукты' and wish == 'фермерское':
    print('Экоферма')
if category == 'молочные продукты' and wish != 'фермерское':
    print( 'Моё село')
if category == 'хлеб' and wish == 'цельнозерновой':
    print ('Пекарня дяди Коли')
if category == 'хлеб' and wish != 'цельнозерновой':
    print("Хлебозавод N°21")