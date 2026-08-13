def squares_and_evens():
    print("Squares of numbers from 1 to 10:")
    for i in range(1, 11):
        print(f"{i}^2 = {i*i}")

    print("\nEnter 5 numbers:")
    numbers = []

    for _ in range(5):
        try:
            num = int(input("Number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input, please enter an integer.")

    even_count = sum(1 for n in numbers if n % 2 == 0)
    print("\nYou entered:", numbers)
    print("Number of even values:", even_count)

squares_and_evens()
