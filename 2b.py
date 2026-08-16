nested_tuple = (
    ("Python for Machine Learning", 401),
    ("Operating Systems", 402),
    ("Scala Programming", 403)
)

sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])

print("Sorted Subjects (by subject code):", sorted_subjects)
