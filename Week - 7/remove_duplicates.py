n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(input("Enter element: "))

new_lst = []
for item in lst:
    if item not in new_lst:
        new_lst.append(item)

print("List after removing duplicates:", new_lst)