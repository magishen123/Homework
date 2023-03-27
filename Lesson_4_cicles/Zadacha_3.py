password = input('put- ')
doc = password.split()


while doc:
    pas = doc.pop(-1)
    if pas == '=' or '?' or '*' or '$' or 'N' or '@' or '_':
        print('Paaword = wrong')
    else:
        print('-')
