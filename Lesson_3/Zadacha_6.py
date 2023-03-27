price_1 = int(input("price_1 - "))
price_2 = int(input("price_2 - "))
price_3 = int(input("price_3 - "))
summa = price_3 + price_2 + price_1

if price_1 < price_2 and price_2 < price_3:
    print(f'Акция  {summa/2}')
elif price_1 > price_2 and price_2 > price_3:
    print(f'Акция  {summa/3}')
else:
    print(f'к оплате  {summa}')