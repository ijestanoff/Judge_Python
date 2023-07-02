# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
word_record = float(input())
distance = float(input())
time_per_meter = float(input())
water_delay = int(distance / 15) * 12.5
ivan_time = distance * time_per_meter + water_delay
if word_record > ivan_time:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.02f} seconds.")
else:
    print(f"No, he failed! He was {ivan_time - word_record:.02f} seconds slower.")