dic = {}
place = input('num>>>')
singer = input('singer>>>')
music = input('mus>>>')


while place != 'off' and singer != 'off' and music != 'off':
    dic[(place, singer)] = music
    place = input('num>>>')
    singer = input('singer>>>')
    music = input('mus>>>')
print(dic)