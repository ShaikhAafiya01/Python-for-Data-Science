def student_marks():
    students = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 88,
        "Eva": 95
    }

    print("=== Student Marks ===")
    for name, marks in students.items():
        print(f"{name}: {marks}")

    average = sum(students.values()) / len(students)
    print("\nClass Average:", average)

    top_student = max(students, key=students.get)
    print("Top Student:", top_student, "with", students[top_student], "marks")

student_marks()
