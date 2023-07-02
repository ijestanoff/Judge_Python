stadium_capacity = int(input())
total_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for number in range(total_fans):
    fan_sector = input()
    if fan_sector == "A":
        sector_a += 1
    elif fan_sector == "B":
        sector_b += 1
    elif fan_sector == "V":
        sector_v += 1
    elif fan_sector == "G":
        sector_g += 1
print(f"{sector_a / total_fans * 100:.2f}%")
print(f"{sector_b / total_fans * 100:.2f}%")
print(f"{sector_v / total_fans * 100:.2f}%")
print(f"{sector_g / total_fans * 100:.2f}%")
print(f"{total_fans / stadium_capacity * 100:.2f}%")