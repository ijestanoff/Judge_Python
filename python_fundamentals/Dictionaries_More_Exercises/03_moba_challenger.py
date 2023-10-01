moba_games = {}
while True:
    command = input()
    if command == "Season end":
        break
    if " -> " in command:
        pps = command.split(" -> ")
        player, position, skill = pps[0], pps[1], int(pps[2])
        if player not in moba_games:
            moba_games[player] = {position: skill}
        elif position not in moba_games[player]:
            moba_games[player][position] = skill
        else:
            if skill > moba_games[player][position]:
                moba_games[player][position] = skill
    if " vs " in command:
        player1, player2 = command.split(" vs ")
        if player1 in moba_games and player2 in moba_games:
            for position in moba_games[player1]:
                if position in moba_games[player2]:
                    player1_total = sum(moba_games[player1].values())
                    player2_total = sum(moba_games[player2].values())
                    if player1_total > player2_total:
                        del moba_games[player2]
                        break
                    elif player2_total > player1_total:
                        del moba_games[player1]
                        break

players_total = {}
for player in moba_games:
    players_total[player] = sum(moba_games[player].values())
players_total = dict(sorted(players_total.items(), key=lambda x: (-x[1], x[0])))
for player, total in players_total.items():
    print(f"{player}: {total} skill")
    sorted_position = dict(sorted(moba_games[player].items(), key=lambda x: (-x[1], x[0])))
    for key, val in sorted_position.items():
        print(f"- {key} <::> {val}")
