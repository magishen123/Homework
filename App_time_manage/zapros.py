import mane

#основная. запросы от пользователи
qesttion = input('Как только наиграетесь введите "все"')

while qesttion != 'все':
    print(mane.zapros(qesttion))
    qesttion = input('Как только наиграетесь введите "все"')

print('Прощайте, возврашайтесь как только захотите')