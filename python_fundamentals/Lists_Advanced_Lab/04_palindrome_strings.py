words_list = input().split()
palindrome = input()
palindrome_list = [words for words in words_list if words==words[::-1]]
number = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {number} times")