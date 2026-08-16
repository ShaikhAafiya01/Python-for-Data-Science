subject1 = ("Python for Machine Learning", 401)
subject2 = ("Operating Systems", 402)
subject3 = ("Scala Programming", 403)

nested_tuple = (subject1, subject2, subject3)
print("Nested Tuple:", nested_tuple)

print("First subject tuple:", nested_tuple[0])
print("Name of second subject:", nested_tuple[1][0])

print("Last subject tuple (negative index):", nested_tuple[-1])
print("Name of last subject:", nested_tuple[-1][0])

print("\nAll Subjects:")
for subject in nested_tuple:
    print(f"Subject Name: {subject[0]}, Code: {subject[1]}")

reversed_tuple = nested_tuple[::-1]
print("\nReversed Tuple:", reversed_tuple)

sliced_tuple = nested_tuple[0:2]
print("Sliced Tuple (first two subjects):", sliced_tuple)

subject4 = ("Computer Networks", 404)
updated_tuple = nested_tuple + (subject4,)
print("After Concatenation:", updated_tuple)

try:
    nested_tuple[0][1] = 999
except TypeError as e:
    print("\nTuple Immutability Test: Error occurred ->", e)
