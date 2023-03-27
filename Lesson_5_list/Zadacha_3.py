mark = input('>>>')
num = 0
five = 0
al = 0

all_marks = mark.split()
five = all_marks.count('5')
num = len(all_marks)
al = five / (num / 100)

print(al)