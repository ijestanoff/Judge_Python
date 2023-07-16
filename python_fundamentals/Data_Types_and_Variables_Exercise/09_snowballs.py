snowballs_number = int(input())
snowball_value = 0
for count in range(snowballs_number):
    weight = int(input())
    target_time = int(input())
    quality = int(input())
    value = (weight / target_time) ** quality
    if value > snowball_value:
        snowball_value = int(value)
        snowball_quality = quality
        snowball_weight = weight
        snowball_time = target_time
print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")

