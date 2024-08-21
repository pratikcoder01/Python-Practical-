# a) Create
print("Creating tuples:")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# b) Access
print("\nAccessing elements from tuples:")
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])
print("Slice of tuple1 (index 1 to 3):", tuple1[1:4])

# c) Update (indirectly)
print("\nUpdating tuple elements (indirectly):")
# Convert tuple to list, update, and convert back to tuple
list1 = list(tuple1)
list1[0] = 10
tuple1 = tuple(list1)
print("Updated tuple1:", tuple1)

# d) Delete
print("\nDeleting a tuple:")
del tuple1
print("Tuple1 deleted. Attempting to print tuple1 will result in an error.")
try:
    print(tuple1)
except NameError as e:
    print(e)
