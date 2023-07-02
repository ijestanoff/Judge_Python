total_sum = 0
while True:
    entered_text = input()
    if entered_text == "NoMoreMoney":
        break
    else:
        money_added = float(entered_text)
        if money_added > 0:
            print(f"Increase: {money_added:.2f}")
            total_sum += money_added
        else:
            print("Invalid operation!")
            break
print(f"Total: {total_sum:.2f}")