summa = 0
fin_cost = 0
sale = 0
while True:
    cost = int(input('-'))
    if cost == 0:
        break
    else:
        summa += cost

if summa % 2 == 0:
    while True:
        if summa % 2 == 0:
            summa = summa // 2
        else:
            break
    print(f'К оплате: {summa}')
else:
    sale = summa * 15 / 100
    fin_cost = summa - sale
    print(f'К оплате: {fin_cost}')