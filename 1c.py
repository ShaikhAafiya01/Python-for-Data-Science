import math

def compute_square_roots():
    print("Enter numbers one by one (type 'done' to finish):")
    while True:
        user_input = input("Number: ")

        if user_input.lower() == "done":
            break

        try:
            number = float(user_input)
            if number < 0:
                print("Cannot compute square root of a negative number.")
            else:
                result = math.sqrt(number)
                print(f"Square root of {number} is {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

compute_square_roots()
