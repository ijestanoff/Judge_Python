team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
card_list = input().split(" ")
game_terminated = False
for card in card_list:
    if card[:1:] == "A":
        if int(card[2::]) in team_A:
            team_A.remove(int(card[2::]))
    else:
        if int(card[2::]) in team_B:
            team_B.remove(int(card[2::]))
    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_terminated:
    print("Game was terminated")


