vet_1 = int(input('>>>'))
vet_2 = int(input('>>>'))
vet_3 = int(input('>>>'))
def vetochka(vet_1,vet_2,vet_3):
    if (vet_1 + vet_2) > vet_3 and (vet_3 + vet_2) > vet_1 and (vet_3 + vet_1) > vet_2:
        return True
    else:
        return False

a = vetochka(vet_1,vet_2,vet_3)
