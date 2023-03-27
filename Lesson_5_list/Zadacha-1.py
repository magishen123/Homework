game = input('')
all_games = []

while game != '0':
    if game in all_games == True:
        print('Thise game ALREADE IN LIST')
    else:
        all_games.append(game)
    game = input('')
    print(all_games)

all_games.sort()
print(all_games)