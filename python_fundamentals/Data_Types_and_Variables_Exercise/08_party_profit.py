group_size = int(input())
days = int(input())
coin_earn = 0
for day_count in range(1, days + 1):
    if day_count % 10 == 0:
        group_size -= 2
    if day_count % 15 == 0:
        group_size += 5
    coin_earn += 50
    coin_earn -= group_size * 2
    if day_count % 3 == 0:
        coin_earn -= group_size * 3
    if day_count % 5 == 0:
        coin_earn += group_size * 20
        if day_count % 3 == 0:
            coin_earn -= group_size * 2
print(f"{group_size} companions received {coin_earn//group_size} coins each.")
