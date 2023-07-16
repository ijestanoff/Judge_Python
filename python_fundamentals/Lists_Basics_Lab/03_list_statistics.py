numbers = int(input())
list_negative = []
list_positive = []
count_positive = 0
sum_negative = 0
for count in range(numbers):
    current_number = int(input())
    if current_number >= 0:
        list_positive.append(current_number)
        count_positive += 1
    else:
        list_negative.append(current_number)
        sum_negative += current_number
print(list_positive)
print(list_negative)
print(f"Count of positives: {count_positive}\nSum of negatives: {sum_negative}")
