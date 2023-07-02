tournament_days = int(input())
money_win = 0
win_count = 0
lose_count = 0
money_day = 0
day_win = 0
day_lose = 0
for count in range(tournament_days):
    while True:
        command = input()
        if command == "Finish":
            if win_count > lose_count:
                money_day *= 1.1
                day_win += 1
            else:
                day_lose += 1
            win_count = 0
            lose_count = 0
            money_win += money_day
            money_day = 0
            break
        sport = command
        state = input()
        if state == "win":
            money_day += 20
            win_count += 1
        elif state == "lose":
            lose_count += 1

if day_win > day_lose:
    money_win *= 1.2
    print(f"You won the tournament! Total raised money: {money_win:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_win:.2f}")