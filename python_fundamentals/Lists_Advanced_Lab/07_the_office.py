happiness = input().split()
improvement_factor = input()
happiness_list = [int(happy) * int(improvement_factor) for happy in happiness]
total_count = len(happiness_list)
average_happiness = sum(happiness_list) / total_count
happy_count = 0
for happiness in happiness_list:
    if happiness >= average_happiness:
        happy_count += 1
if happy_count >= total_count / 2:
    string_happy = 'Employees are happy!'
else:
    string_happy = 'Employees are not happy!'
print(f"Score: {happy_count}/{total_count}. {string_happy}")
