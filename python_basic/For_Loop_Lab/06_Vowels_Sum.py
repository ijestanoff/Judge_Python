# буква	    a	e	i	o	u
# стойност	1	2	3	4	5
inp_str = input()
total_sum = 0
for count in inp_str:
    if count == "a":
        total_sum += 1
    elif count == "e":
        total_sum += 2
    elif count == "i":
        total_sum += 3
    elif count == "o":
        total_sum += 4
    elif count == "u":
        total_sum += 5
print(total_sum)
