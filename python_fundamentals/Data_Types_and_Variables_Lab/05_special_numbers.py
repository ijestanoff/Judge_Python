number = int(input())
for count in range(1, number + 1):
    total = 0
    type_number = False
    for cnt in str(count):
        total += int(cnt)
    if total == 5 or total == 7 or total == 11:
        type_number = True
    print(f"{count} -> {type_number}")
