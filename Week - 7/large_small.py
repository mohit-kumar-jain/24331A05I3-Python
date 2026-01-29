n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

largest = max(lst)
smallest = min(lst)

print("Largest number in the list is :", largest)
print("Smallest number in the list is :", smallest)