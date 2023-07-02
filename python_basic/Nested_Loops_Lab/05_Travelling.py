while True:
    destination = input()
    if destination == "End":
        break
    destination_sum = float(input())
    current_sum = 0
    while current_sum < destination_sum:
        input_sum = float(input())
        current_sum += input_sum
    print(f"Going to {destination}!")