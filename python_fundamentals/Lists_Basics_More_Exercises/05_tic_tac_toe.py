row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
col_1 = [row_1[0], row_2[0], row_3[0]]
col_2 = [row_1[1], row_2[1], row_3[1]]
col_3 = [row_1[2], row_2[2], row_3[2]]
first_player_won = False
second_player_won = False
if row_1.count("1") == 3 or row_2.count("1") == 3 or row_3.count("1") == 3 or \
        col_1.count("1") == 3 or col_2.count("1") == 3 or col_3.count("1") == 3:
    first_player_won = True
elif row_1.count("2") == 3 or row_2.count("2") == 3 or row_3.count("2") == 3 or \
        col_1.count("2") == 3 or col_2.count("2") == 3 or col_3.count("2") == 3:
    second_player_won = True
elif row_1[0] == "1" and row_2[1] == "1" and row_3[2] == "1" or row_1[2] == "1" and row_2[1] == "1" and row_3[0] == "1":
    first_player_won = True
elif row_1[0] == "2" and row_2[1] == "2" and row_3[2] == "2" or row_1[2] == "2" and row_2[1] == "2" and row_3[0] == "2":
    second_player_won = True
if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")
