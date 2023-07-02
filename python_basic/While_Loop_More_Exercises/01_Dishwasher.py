number_of_bottles = int(input())
detergent_amount = number_of_bottles * 750
dish_count = 0
clean_dish = 0
clean_pot = 0
while True:
    command = input()
    if command == "End":
        print("Detergent was enough!")
        print(f"{clean_dish} dishes and {clean_pot} pots were washed.")
        print(f"Leftover detergent {detergent_amount} ml.")
        break
    amount = int(command)
    if dish_count < 2:
        dish_count += 1
        detergent_amount -= amount * 5
        clean_dish += amount
    else:
        dish_count = 0
        detergent_amount -= amount * 15
        clean_pot += amount
    if detergent_amount < 0:
        print (f"Not enough detergent, {-detergent_amount} ml. more necessary!")
        break





