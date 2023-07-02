# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
from math import ceil
serial_name = input()
episode_time = int(input())
pause_time = int(input())
launch_time = pause_time / 8
relax_time = pause_time / 4
time_left = pause_time - (launch_time + relax_time)
if time_left >= episode_time:
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_left-episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(episode_time - time_left)} more minutes.")