def is_Palindrome(s):
    return s == s[::-1]
word = input("Enter String: ")

if (is_Palindrome(word)):
    print("This word is a palindrom")
else:
    print("This word is NOT a palindrom")
    