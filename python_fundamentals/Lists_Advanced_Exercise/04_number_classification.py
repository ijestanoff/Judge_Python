number_list = input().split(", ")
positive_list = [number for number in number_list if int(number) >= 0]
negative_list = [number for number in number_list if int(number) < 0]
even_list = [number for number in number_list if int(number) % 2 == 0]
odd_list = [number for number in number_list if int(number) % 2 != 0]
print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")

