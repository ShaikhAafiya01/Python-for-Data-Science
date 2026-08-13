def list_operations():

    numbers = [12, 45, 7, 23, 89, 34, 56, 78, 10, 5]
    print("Original list:", numbers)

    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)

    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", average)

    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)

    print("Ascending order:", ascending)
    print("Descending order:", descending)

    numbers.append(100)
    print("After adding 100:", numbers)

    numbers.pop(0)
    print("After removing first item:", numbers)

list_operations()
