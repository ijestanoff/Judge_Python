import sys
low_number = sys.maxsize
while True:
    text_entered = input()
    if text_entered == "Stop":
        print(low_number)
        break
    number = int(text_entered)
    if number < low_number:
        low_number = number

