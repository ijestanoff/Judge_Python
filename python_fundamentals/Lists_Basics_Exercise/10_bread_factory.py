energy = 100
coins = 100
event_list = input().split("|")
closed_event = False
for count in range(len(event_list)):
    event = event_list[count].split("-")
    event_quantity = int(event[1])
    if event[0] == "rest":
        new_energy = energy + event_quantity
        if new_energy > 100:
            new_energy = 100
        print(f"You gained {new_energy - energy} energy.")
        energy = new_energy
        print(f"Current energy: {energy}.")
    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += event_quantity
            print(f"You earned {event_quantity} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_quantity:
            coins -= event_quantity
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            closed_event = True
            break
if not closed_event:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
