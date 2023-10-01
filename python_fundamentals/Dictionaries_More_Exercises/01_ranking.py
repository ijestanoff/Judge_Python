contests = {}
ranking = {}
while True:
    command = input().split(":")
    if command[0] == "end of contests":
        break
    contest, password = command
    contests[contest] = password

while True:
    command = input().split("=>")
    if command[0] == "end of submissions":
        break
    contest, password, username, points = command
    points = int(points)
    if contest in contests and contests[contest] == password:
        if username not in ranking:
            ranking[username] = {}
            ranking[username][contest] = points
        else:
            if contest not in ranking[username]:
                ranking[username][contest] = points
            elif points > ranking[username][contest]:
                ranking[username][contest] = points

max_points = 0
max_user = ''
for user, language in ranking.items():
    if sum(language.values()) > max_points:
        max_points = sum(language.values())
        max_user = user
print(f"Best candidate is {max_user} with total {max_points} points.")
print("Ranking:")
user_sort = sorted(ranking.keys())
for user in user_sort:
    print(user)
    language = ranking[user]
    while len(language) > 0:
        max_points_value = -1
        max_points_key = ''
        for key, val in language.items():
            if val > max_points_value:
                max_points_value = val
                max_points_key = key
        print(f"#  {max_points_key} -> {max_points_value}")
        del language[max_points_key]

