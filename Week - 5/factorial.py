#  With Recursion

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
n = int(input("Enter a number to find factorial : "))
print(f"The factorial of {n} is {factorial(n)}.")


#  Without Recursion

# n = int(input("Enter a number to find factorial : "))
# def factorial(n):
#     fact = 1
#     for i in range n+1:
#         fact *= i
        
#     return fact
# print(f"The factorial of {n} is {factorial(n)}.")