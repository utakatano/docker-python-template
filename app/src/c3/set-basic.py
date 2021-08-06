colors = {'red', 'green', 'blue'}

print(colors)

e = set()

print(e)

fruits = set({"orange", "banana", "mango"})

print(fruits)

box1 = {'hammer', 'nail', 'plier'}

box2 = {'nail', 'plier'}

print(box1 - box2)

print('plier' in box1)

team1 = {'endo', 'sato', 'nakamura'}

team2 = {'tanaka', 'endo', 'nakamura'}

team3 = team1 | team2
print(team3)

team4 = team1 & team2
print(team4)