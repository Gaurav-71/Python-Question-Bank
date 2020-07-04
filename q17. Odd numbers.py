numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]


def count(list):
    return len([item for item in list if item % 2 != 0])


print("Number of odd numbers :", count(numbers))
