year = int(input())
while True:
    year += 1
    check_year = str(year)
    if len(check_year) == len(set(check_year)):
        break
print(year)

