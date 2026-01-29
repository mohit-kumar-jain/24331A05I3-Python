lst = []

n = int(input("Enter number of elements: "))
for i in range(n):
    lst.append(input("Enter element: "))

print("Length of the List is :",len(lst))

m = int(input("Enter number of elements to extend: "))
ext = []
for i in range(m):
    ext.append(input("Enter element: "))
lst.extend(ext)
print("The extended list is :",lst)

lst.sort()
print("The sorted list is :",lst)

item = input("Enter element to append: ")
lst.append(item)
print("After append the list is :",lst)

pos = int(input("Enter position to insert: "))
val = input("Enter element to insert: ")
lst.insert(pos, val)
print("The list after insertion is :",lst)

rem = input("Enter element to remove: ")
lst.remove(rem)
print("The list after removing element is :",lst)