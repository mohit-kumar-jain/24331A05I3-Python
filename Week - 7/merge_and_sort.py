n1 = int(input("Enter number of elements in first list: "))
list1 = []

for i in range(n1):
    list1.append(int(input(f"Enter {i+1} element: ")))

n2 = int(input("Enter number of elements in second list: "))
list2 = []

for i in range(n2):
    list2.append(int(input(f"Enter {i+1} element: ")))

merged_lst = list1 + list2
merged_lst.sort()

print("Merged and sorted list:", merged_lst)