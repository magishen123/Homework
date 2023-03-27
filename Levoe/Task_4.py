word = input('>>')
word.split()
fin = reversed(word)
if word == fin:
    print(bool(0))
else:
    print(bool(1))