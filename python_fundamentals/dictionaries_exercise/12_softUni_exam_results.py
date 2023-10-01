judge_stat = {}
submissions = {}
while True:
    command = input().split("-")
    if command[0] == "exam finished":
        break
    if command[1] == "banned":
        username = command[0]
        if username not in judge_stat:
            judge_stat[username] = {}
        judge_stat[username]['banned'] = "yes"
    else:
        username, language, points = command[0], command[1], int(command[2])
        if username not in judge_stat:
            judge_stat[username] = {language: points}
        elif language in judge_stat[username]:
            max_point = max(judge_stat[username][language], points)
            judge_stat[username][language] = max_point
        else:
            judge_stat[username][language] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for name in judge_stat:
    if "banned" not in judge_stat[name]:
        for lang in judge_stat[name]:
            print(f"{name} | {judge_stat[name][lang]}")
            break

print("Submissions:")
for language in submissions:
    print(f"{language} - {submissions[language]}")




