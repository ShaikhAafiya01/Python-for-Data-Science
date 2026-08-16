my_tuple = ("Java", 101, 3.14, True, "Networking")
print("Tuple with 5 elements:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

middle_slice = my_tuple[1:4]
print("Middle 3 elements:", middle_slice)

tuple1 = ("Python", "Scala")
tuple2 = ("Linux", "Windows")
concatenated = tuple1 + tuple2
print("Concatenated Tuple:", concatenated)

reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)

count_tuple = ("Python", "Python", "Scala", "Python", "Java")
print("Count of 'Java':", count_tuple.count("Java"))

print("Index of 'Python':", count_tuple.index("Python"))

print("'Scala' exists in tuple?", "Scala" in count_tuple)

my_list = ["AI", "ML", "DL"]
converted_tuple = tuple(my_list)
print("Converted Tuple:", converted_tuple)

num_tuple = (45, 12, 78, 34, 23)
sorted_tuple = tuple(sorted(num_tuple))
print("Sorted Tuple:", sorted_tuple)

repeat_tuple = ("Cloud", "DevOps") * 3
print("Repeated Tuple:", repeat_tuple)

immutable_tuple = ("Database", 999)

try:
    immutable_tuple[1] = 1000
except TypeError as e:
    print("Tuple is immutable! Error:", e)
