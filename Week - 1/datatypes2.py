num  = 10
print("Original Integer :",num)
num += 5
print("Modified Integer :",num)
print("Memory Address of num is:",id(num))

str = "Hello"
print("Original string  :",str)
str += " World"
print("Modified string :",str)
print("Memory Address of str is:",id(str))

tup = (1,2,3)
print("Original tuple :",tup)

lst = [1,2,3]
print("Original List :",lst)
lst.append(4)
print("Modified List :",lst)
print("Memory Address of str is:",id(lst))


dict = {"a":1,"b" : 2}
print("Original dictionary :",dict)
dict["c"] = 3
print("Modified List :",dict)
print("Memory Address of str is:",id(dict))