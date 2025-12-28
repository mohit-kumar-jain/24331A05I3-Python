num = int(input("Enter a number: "))
x = num
n = len(str(num))
add = 0
temp = num
while temp > 0:
    digit = temp % 10         
    add += digit ** n  
    temp //= 10               
if add == x:
    print(f"{x} is an Armstrong number.")
else:
    print(f"{x} is not an Armstrong number.")