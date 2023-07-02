TOM_GAME_LEVEL = 30000
WORK_DAY_PLAY = 63
REST_DAY_PLAY = 127
rest_day = int(input())
game_time = rest_day * REST_DAY_PLAY + (365 - rest_day) * WORK_DAY_PLAY
if game_time > TOM_GAME_LEVEL:
    difference_time = game_time - TOM_GAME_LEVEL
    print(f"Tom will run away\n{difference_time // 60} hours and {difference_time % 60} minutes more for play")
else:
    difference_time = TOM_GAME_LEVEL - game_time
    print(f"Tom sleeps well\n{difference_time // 60} hours and {difference_time % 60} minutes less for play")