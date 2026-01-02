#  With Recursion

# def is_prime(n,i=2):
#     if n<=1:
#         return False
#     if i*i>n:
#         return True
#     if n%i==0:
#         return False
#     return is_prime(n,i+1)
# n = int(input("Enter a number to check prime (or) not : "))
# print(f"{n} is a prime number."if is_prime(n) else f"{n} is not a prime number.")


#  Without Recursion

n = int(input("Enter a number to check prime (or) not : "))
def is_prime(n,i=2):
    for i in range(2,int(n**0.5)+1):
        if n<=1:
            return False
        if n%i==0:
            return False
        return True
print(f"{n} is a prime number."if is_prime(n) else f"{n} is not a prime number.")   