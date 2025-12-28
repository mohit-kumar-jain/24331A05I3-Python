a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
print("The maximum of three numbers is : ")
if (a>=b and a>=c):
    print(f"{a} is greater than {b} and {c}.")
elif (b>=a and b>=c):
    print(f"{b} is greater than {a} and {c}.")
else:
    print(f"{c} is greater than {a} and {b}.")
print("The minimum of three numbers is : ")
if (a<=b and a<=c):
    print(f"{a} is smaller than {b} and {c}.")
elif (b<=a and b<=c):
    print(f"{b} is smaller than {a} and {c}.")
else:
    print(f"{c} is smaller than {a} and {b}.")