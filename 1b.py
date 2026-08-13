def add_numbers():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    total = sum(numbers)

    print("The total is:", total)

add_numbers()
