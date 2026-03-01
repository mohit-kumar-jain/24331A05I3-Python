num = (1, 2, 3, 4, 5)
tple = tuple(num)
print("The Tuple is : ",tple)

square_tple = tuple(x**2 for x in num)
print("The Squared Tuple is : ",square_tple)

even_tple = tuple(x for x in range(10) if x % 2 == 0)
print("The Even Tuple is : ",even_tple)