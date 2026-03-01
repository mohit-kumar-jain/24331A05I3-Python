dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"d": 4}
print(f"The dictornay (dct1) key - value pairs are: {dct1}")
print(f"The dictornay (dct2) key - value pairs are: {dct2}")

keys = dct1.keys()
values = dct1.values()
items = dct1.items()

print("Keys in the dct1 are :", list(keys))
print("Values in the dct1 are :", list(values))
print("Items in the dct1 are:", list(items))

a1 = dct1.get("a")
print(f"The value at key a is : {a1}.")

z = dct1.get("z", 0)
print(f"The value at key z is : {z}.")

dct1.update(dct2)
dct1.update([("e", 5)])
print(f"The dct1 after update is  : {dct1}.")

pop_val = dct1.pop("b")
pop_item = dct1.popitem()
print(f"The poped key,value pair  is  : {pop_item}.")
print("Final Dict is:", dct1)
