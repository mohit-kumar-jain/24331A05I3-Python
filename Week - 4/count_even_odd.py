a = int(input("Enter the range of numbers from 1 to ?: "))
odd = 0
even = 0
for i in range (1,a+1):
    if (i%2 != 0):
        odd +=1
    else:
        even+=1  
print("The number of odd numbers are : ",odd)
print("The number of even numbers are : ",even)