number_of_tournaments = int(input())
starting_points = int(input())
final_points = starting_points
average_points = 0
tournament_wins = 0
for count in range(0, number_of_tournaments, 1):
    stage = input()
    if stage == "W":
        final_points += 2000
        tournament_wins += 1
    elif stage == "F":
        final_points += 1200
    elif stage == "SF":
        final_points += 720
print(f"Final points: {final_points}")
average_points = int((final_points - starting_points) / number_of_tournaments)
print(f"Average points: {average_points}")
print(f"{tournament_wins / number_of_tournaments * 100:.2f}%")
