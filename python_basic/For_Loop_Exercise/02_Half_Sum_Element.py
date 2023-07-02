number = int(input())
max_element = 0
sum_elements = 0
for count in range(0, number, 1):
    element = int(input())
    sum_elements += element
    if element > max_element:
        max_element = element
if sum_elements - max_element == max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    print("No")
    diff = abs(max_element - (sum_elements - max_element))
    print(f"Diff = {diff}")
