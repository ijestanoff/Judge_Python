number_of_turns = int(input())
result = 0
invalid_number = 0
up_9 = 0
up_19 =0
up_29 = 0
up_39 = 0
up_50 = 0
for number in range(number_of_turns):
    current_number = int(input())
    if current_number < 0 or current_number > 50:
        result /= 2
        invalid_number += 1
    elif 0 <= current_number <= 9:
        result += current_number * 0.2
        up_9 += 1
    elif current_number <= 19:
        result += current_number * 0.3
        up_19 += 1
    elif current_number <= 29:
        result += current_number * 0.4
        up_29 += 1
    elif current_number <= 39:
        result += 50
        up_39 += 1
    elif current_number <=50:
        result += 100
        up_50 += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {up_9 / number_of_turns * 100:.2f}%")
print(f"From 10 to 19: {up_19 / number_of_turns * 100:.2f}%")
print(f"From 20 to 29: {up_29 / number_of_turns * 100:.2f}%")
print(f"From 30 to 39: {up_39 / number_of_turns * 100:.2f}%")
print(f"From 40 to 50: {up_50 / number_of_turns * 100:.2f}%")
print(f"Invalid numbers: {invalid_number / number_of_turns * 100:.2f}%")



