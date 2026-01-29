def Sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [1, 2, 3, 4 ,5]
print("The sum of given elements in the list is :",Sum_of_list(my_list))