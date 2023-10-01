words = {}
count = int(input())
for cnt in range(count):
    word = input()
    synonym = input()
    if word not in words:
        words[word] = []
    words[word].append(synonym)

for word in words:
    print(f"{word} - {', '.join(words[word])}")