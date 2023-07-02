minutes_run_per_day = int(input())
runs_per_day = int(input())
calories_for_day = int(input())
total_calories_for_run = minutes_run_per_day * runs_per_day * 5
if total_calories_for_run >= calories_for_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_for_run}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_for_run}.")


