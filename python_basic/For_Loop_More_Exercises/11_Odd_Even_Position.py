MAXIMUM = 999999999999999999
odd_sum = 0
odd_min = MAXIMUM
odd_max = -MAXIMUM
even_sum = 0
even_min = MAXIMUM
even_max = -MAXIMUM
numbers = int(input())
for count in range(numbers):
    current_number = float(input())
    if count % 2 == 0:
        odd_sum += current_number
        if current_number < odd_min:
            odd_min = current_number
        if current_number > odd_max:
            odd_max = current_number
    else:
        even_sum += current_number
        if current_number < even_min:
            even_min = current_number
        if current_number > even_max:
            even_max = current_number
print(f"OddSum={odd_sum:.2f},")
if odd_min == MAXIMUM:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -MAXIMUM:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == MAXIMUM:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -MAXIMUM:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
