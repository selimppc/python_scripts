"""
Top 10 beginner Python code challenges
"""

# 1.
def radians_to_degrees(radians):
    return radians * (180 / 3.14159265358979323846)  # we can use math.pi as return radians * (180 / math.pi) # noqa
print(radians_to_degrees(3.14159265358979323846))

# 2.
def sort_list(numbers, order):
    """
    If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
    :param numbers:
    :param order:
    :return:
    """

    if order == 'asc':
        return sorted(numbers)
    elif order == 'desc':
        return sorted(numbers, reverse=True)
    else:
        return numbers

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
ascending = sort_list(numbers, "asc")
descending = sort_list(numbers, "desc")
original = sort_list(numbers, "none")

print("Ascending:", ascending)
print("Descending:", descending)
print("Original:", original)
