footballers_goals = {'Eusebio': 120, 'Cruyff': 120, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
footballers_goals = dict(sorted(footballers_goals.items(), key=lambda x: (-x[1], x[0])))

print(footballers_goals)

a = "Kolio"
b = "Gosho"
print(id(a))
print(id(b))