import random

players = ['oktay', 'umit', 'musty', 'ali', 'ozayyildiz', 'kerem', 'goksel', 'okan', 'recep', 'mupo']

MIN = 0
team_A = ['memo']
team_B = ['kaleci']

for i in range(MIN, len(players)-1):
  index = random.randint(MIN, len(players)-1)
  team_A.append(players[index])
  players.pop(index)
  index2 = random.randint(MIN, len(players)-1)
  team_B.append(players[index2])
  players.pop(index2)
  if len(players) == 0:
    break
    
print('------------------------------------------------------------')
print(team_A)
print('------------------------------------------------------------')
print(team_B)