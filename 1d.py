def swap_elements(lst, index1, index2):

    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


numbers = [10, 20, 30, 40]
print("Original list:", numbers)

updated_list = swap_elements(numbers, 1, 3)
print("Updated list:", updated_list)
