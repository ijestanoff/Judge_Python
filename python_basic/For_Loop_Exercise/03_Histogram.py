number = int(input())
p_0_199 = 0
p_200_399 = 0
p_400_599 = 0
p_600_799 = 0
p_800_1000 = 0
for count in range(0, number, 1):
    element = int(input())
    if element < 200:
        p_0_199 += 1
    elif element < 400:
        p_200_399 += 1
    elif element < 600:
        p_400_599 += 1
    elif element < 800:
        p_600_799 += 1
    else:
        p_800_1000 += 1
print(f"{(p_0_199/number)*100:.2f}%")
print(f"{(p_200_399/number)*100:.2f}%")
print(f"{(p_400_599/number)*100:.2f}%")
print(f"{(p_600_799/number)*100:.2f}%")
print(f"{(p_800_1000/number)*100:.2f}%")
