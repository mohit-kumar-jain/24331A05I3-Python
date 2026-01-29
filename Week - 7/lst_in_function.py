def Display(lst):
    for item in lst:
        print(item)

n = int(input("Enter number of elements: "))
n_list = []

for i in range(n):
    n_list.append(input("Enter element: "))

Display(n_list)