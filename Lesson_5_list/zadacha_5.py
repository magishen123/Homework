num = input('>>')
all_num = num.split()
n = 0
a = 0

if len(all_num) == 1:
    print('nepravilno')
else:
    for chislo in all_num:
        n += 1
        a = all_num[n]
        a = int(a)
        chislo = int(chislo)
        print(n, a, chislo, all_num)
        if chislo - a == -1:
            print('ok')
        else:
            break



