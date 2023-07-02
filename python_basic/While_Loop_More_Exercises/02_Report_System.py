charity_sum = int(input())
payment_type = 0
card_total = 0
cash_total = 0
cash_counter = 0
card_counter =0
while True:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    payment = int(command)
    if not payment_type:
        payment_type = 1
        if payment <= 100:
            cash_total += payment
            cash_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        payment_type = 0
        if payment >= 10:
            card_total += payment
            card_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    if card_total + cash_total >= charity_sum:
        print(f"Average CS: {cash_total / cash_counter:.2f}")
        print(f"Average CC: {card_total / card_counter:.2f}")
        break

