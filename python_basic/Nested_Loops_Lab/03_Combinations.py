total_sum = int(input())
combination_counter = 0
for x1 in range(total_sum + 1):
    for x2 in range(total_sum + 1):
        for x3 in range(total_sum + 1):
            if x1 + x2 + x3 == total_sum:
                combination_counter += 1
print(combination_counter)