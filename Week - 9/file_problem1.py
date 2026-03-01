file = open("sample.txt", "w")

file.write("Hello World\n")
file.write("Welcome to Python File Handling\n")


file.writelines(["This is line 3\n", 
                 "This is line 4\n", 
                 "This is line 5\n"])

file.close()

file = open("sample.txt", "r")
print("Using read():")
print(file.read())     
file.close()

file = open("sample.txt", "r")
print("Using readline():")
print(file.readline())  
print(file.readline())  
file.close()

file = open("sample.txt", "r")
print("Using readlines():")
print(file.readlines())  
file.close()