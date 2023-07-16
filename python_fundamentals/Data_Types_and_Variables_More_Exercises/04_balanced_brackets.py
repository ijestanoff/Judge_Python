lines_number = int(input())
open_bracket = False
balanced = True
for count in range(lines_number):
    line = input()
    if line == "(" and not open_bracket:
        open_bracket = True
    elif line == "(" and open_bracket:
        balanced = False
        break
    elif line == ")" and not open_bracket:
        balanced = False
        break
    elif line == ")" and open_bracket:
        open_bracket = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
