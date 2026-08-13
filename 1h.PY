def grade_calculator():
    try:
        marks = int(input("Enter marks: "))

        if marks >= 90:
            grade = "A"
        elif 75 <= marks <= 89:
            grade = "B"
        elif 50 <= marks <= 74:
            grade = "C"
        else:
            grade = "Fail"

        print("Grade:", grade)
    except ValueError:
        print("Invalid input. Please enter numeric marks.")

grade_calculator()
