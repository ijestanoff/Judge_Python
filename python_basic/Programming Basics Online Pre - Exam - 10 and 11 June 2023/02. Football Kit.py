t_shirt_price = float(input())
sum_to_ball = float(input())
shorts_price = 0.75 * t_shirt_price
socks_price = 0.20 * shorts_price
buttons = (t_shirt_price + shorts_price) * 2
total_price = t_shirt_price + shorts_price + socks_price + buttons
total_price = total_price - total_price * 0.15
if total_price >= sum_to_ball:
    print ("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_to_ball - total_price:.2f} lv. more.")
