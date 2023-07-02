# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

cinema_type = input()
cinema_row = int(input())
cinema_column = int(input())
price = 0
if cinema_type == "Premiere":
    price = 12
elif cinema_type == "Normal":
    price = 7.5
elif cinema_type == "Discount":
    price = 5
total_price = cinema_row * cinema_column * price
print (f"{total_price:.2f} leva")

