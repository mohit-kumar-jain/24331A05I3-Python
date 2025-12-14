P = float(input("Enter principal amount : "))
T = float(input("Enter time : "))
R = float(input("Enter rate of interest : "))
A = P * (1 + R/100) ** T
Ci = A - P
print("The result of compound interest is : ",Ci)
print("Principal amount is : ",A)