command = ""
total_steps = 0
while total_steps < 10_000 and command != "Going home":
    command = input()
    if command != "Going home":
        total_steps += int(command)
    else:
        steps_to_home = int(input())
        total_steps += steps_to_home
if total_steps < 10_000:
    print(f"{10000 - total_steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
