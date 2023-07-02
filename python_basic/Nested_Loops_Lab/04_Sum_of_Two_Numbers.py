interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
combination_counter = 0
combination_found = False
for first_number in range(interval_start, interval_end + 1):
    for second_number in range(interval_start, interval_end + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")