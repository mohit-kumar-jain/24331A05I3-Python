s = input("Enter a string: ")
if s == s[::-1]:
    print(f"{s} is Palindrome.")
else:
    print(f"{s} is not a palindrome.")