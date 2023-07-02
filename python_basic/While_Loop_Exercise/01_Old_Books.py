ani_book = input()
book_number = 0
while True:
    new_book = input()
    if ani_book == new_book:
        print(f"You checked {book_number} books and found it.")
        break
    if new_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_number} books.")
        break
    book_number += 1