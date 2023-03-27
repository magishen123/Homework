list_prod = []
summa = 0
while True:
    cost = int(input('-'))
    if cost == 0:
        break
    else:
        sale_cost = cost//1.5 #делит нацело
        summa = sale_cost
        list_prod.append(cost)
print(f'Раюбота завершена, цена = {summa}')