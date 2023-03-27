chislo = int(input('введите число '))
all_chisla = []
summa = 0
n = 0
lucky = 0

while chislo != 0:
    summa += chislo
    n += 1
    chislo = str(chislo)
    all_chisla.append(chislo)
    chislo = int(input('введите число'))

lucky = summa/n*100
print(lucky, n)
print(','.join(all_chisla))