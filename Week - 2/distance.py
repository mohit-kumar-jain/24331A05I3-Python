import math
P1 = int(input("Enter the value of P1: "))
P2 = int(input("Enter the value of P2: "))
S1 = int(input("Enter the value of S1: "))
S2 = int(input("Enter the value of S2: "))
D = math.sqrt(((P2-P1)**2)+((S2-S1)**2))
print("Distance between the two points is : ",D)