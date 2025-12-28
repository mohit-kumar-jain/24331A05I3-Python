a = input("Enter a string or number: ")
if a == a[::-1]:
    print(f"'{a}' is a palindrome.")
else:
    print(f"'{a}' is not a palindrome.")