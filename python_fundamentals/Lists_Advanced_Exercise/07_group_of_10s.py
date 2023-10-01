numbers_list = list(map(int, input().split(", ")))
group = 10
while len(numbers_list) > 0:
    current_list = []
    for number_index in range(len(numbers_list) - 1, -1, -1):
        if numbers_list[number_index] <= group:
            current_list.append(numbers_list[number_index])
            numbers_list.pop(number_index)
    current_list.reverse()
    print(f"Group of {group}'s: {current_list}")
    group += 10
