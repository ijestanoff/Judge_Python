judge = {}
contests = {}
participant_dict = {}
while True:
    command = input().split(" -> ")
    if command[0] == "no more time":
        break
    username, contest, points = command[0], command[1], int(command[2])
    if username not in judge:
        judge[username] = {contest: points}
    elif contest not in judge[username]:
        judge[username][contest] = points
    else:
        if points > judge[username][contest]:
            judge[username][contest] = points
    if contest not in contests:
        contests[contest] = {username: points}
    elif username not in contests[contest]:
        contests[contest][username] = points
    else:
        if points > contests[contest][username]:
            contests[contest][username] = points

for constest_name, participant in contests.items():
    print(f"{constest_name}: {len(participant)} participants")
    sort_participants = dict(sorted(participant.items(), key=lambda x: (-x[1], x[0])))
    number = 1
    for key, val in sort_participants.items():
        print(f"{number}. {key} <::> {val}")
        number += 1

print("Individual standings:")
for participant_name, constest_name in judge.items():
    participant_dict[participant_name] = sum(constest_name.values())
participant_dict = dict(sorted(participant_dict.items(), key=lambda x: (-x[1], x[0])))
number = 1
for key, val in participant_dict.items():
    print(f"{number}. {key} -> {val}")
    number += 1
