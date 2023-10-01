text = input().split()
even_text = [word for word in text if len(word) % 2 == 0]
for word in even_text:
    print(word)

