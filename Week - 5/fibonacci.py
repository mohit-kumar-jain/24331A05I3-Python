#  With Recursion

def fib(n): 
    if n==1 or n==0:
        return n
    return fib(n-1)+fib(n-2)
n = int(input("Enter a number to print fibonacci series : "))
print(f"The fibonacci of series upto {n} is : ",end=" ")
for i in range(n):
    print(fib(i),end=" ")
print()


#  Without Recursion

# def fib(n):
#     a,b = 0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b,a+b
        
        
# n = int(input("Enter a number to print fibonacci series : "))
# print("The fibonacci of series upto ",n," is : ",end=" ")
# fib(n)
