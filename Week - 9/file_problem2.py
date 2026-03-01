file = open("dummy.txt", "w+")

file.write("Hello World!\n")

file.flush()
print("Data flushed to file.")

file.seek(0)
print("Pointer position after seek(0):", file.tell())

data = file.read(5)
print("First 5 characters:", data)

print("Current pointer position:", file.tell())

file.seek(0, 2)
print("Pointer position at end:", file.tell())

file.close()