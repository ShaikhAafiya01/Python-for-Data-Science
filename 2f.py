numbers = [12, 45, 78, 34, 23]
print("Largest number:", max(numbers))

dup_list = [10, 20, 10, 30, 20, 40]
unique_list = list(set(dup_list))
print("List after removing duplicates:", unique_list)

num_list = [5, 12, 7, 18, 21, 24]
even_count = sum(1 for n in num_list if n % 2 == 0)
print("Count of even numbers:", even_count)

user_list = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    user_list.append(num)

print("List of entered numbers:", user_list)

def average(lst):
    return sum(lst) / len(lst)

print("Average of numbers:", average([10, 20, 30, 40, 50]))

my_string = "Python"
char_list = list(my_string)
print("List of characters:", char_list)

words = ["AI", "ML", "DL"]
joined_string = " ".join(words)
print("Joined String:", joined_string)
