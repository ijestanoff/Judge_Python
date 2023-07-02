computer_numbers = int(input())
rating = 0
sales = 0
total_rating = 0
total_sales = 0
for number in range(computer_numbers):
    sells_rating = int(input())
    rating = sells_rating % 10
    sales = (sells_rating - rating) / 10
    if rating == 2:
        sales = 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 1
    total_sales += sales
    total_rating += rating
print(f"{total_sales:.2f}")
print(f"{total_rating / computer_numbers:.2f}")
