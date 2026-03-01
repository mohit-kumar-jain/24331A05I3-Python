stu = {"name": "Mohit", "age": 20, "branch": "CSE"}

val = input("Enter a value to find its key: ")

found = False

for key, value in stu.items():
    if str(value) == val:
        print("Key Found : ", key)
        found = True
        break

if not found:
    print("Value Not Found!!")