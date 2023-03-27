dicte = {1: '1', 2:'2'}
'''def raw():
    name_key = input('прервать ф-цию !')
    chislo_val = input('>>>')
    dicte[name_key] = chislo_val

    while name_key != '!':
        name_key = input('прервать ф-цию !')
        chislo_val = input('>>>')
        dicte[name_key] = chislo_val
        print(dicte)'''

def remen():
    poluchit_remna = input('>>>')
    for i in dicte:
        print(dicte[i])

    print()

remen()


