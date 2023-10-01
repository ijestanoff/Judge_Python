rows = int(input())
ships = [list(input().split()) for i in range(rows)]
for i in range(len(ships[0])):
    for j in range(rows):
        ships[j][i] = int(ships[j][i])
attacks = input().split()
ship_destroyed = 0
for attack in attacks:
    row_col = attack.split('-')
    row, col = int(row_col[0]), int(row_col[1])
    if ships[row][col] > 0:
        ships[row][col] -= 1
        if ships[row][col] == 0:
            ship_destroyed += 1
print(ship_destroyed)
