students = int(input())
low_rating = 0
average_rating = 0
good_rating = 0
excellent_rating = 0
all_rating = 0
for number in range(students):
    rating = float(input())
    all_rating += rating
    if 2 <= rating <= 2.99:
        low_rating += 1
    elif 3 <= rating <= 3.99:
        average_rating += 1
    elif 4 <= rating <= 4.99:
        good_rating += 1
    elif rating >= 5:
        excellent_rating += 1
print(f"Top students: {excellent_rating / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good_rating / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {average_rating / students * 100:.2f}%")
print(f"Fail: {low_rating / students * 100:.2f}%")
print(f"Average: {all_rating / students:.2f}")