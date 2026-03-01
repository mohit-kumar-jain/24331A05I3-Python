import random

with open("rand_num.txt", "w") as file:
    for i in range(10):
        num = random.randint(1, 100)
        file.write(str(num) + "\n")

print("File written successfully\n")

with open("rand_num.txt", "r") as file :
    print("read\n")
    print(file.read())