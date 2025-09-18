# MBPP/824
### Completion
def remove_even(numbers):
    """
    Remove even numbers from the given list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    list: A list containing only the odd integers from the input list.
    """
    # Using list comprehension to filter out even numbers
    return [num for num in numbers if num % 2 != 0]

# Test case
assert remove_even([1, 3, 5, 2]) == [1, 3, 5]

# Additional test cases for verification
assert remove_even([2, 4, 6, 8]) == []  # All even numbers
assert remove_even([1, 2, 3, 4, 5]) == [1, 3, 5]  # Mixed numbers
assert remove_even([]) == []  # Empty list
assert remove_even([0, -1, -2, -3]) == [-1, -3]  # Including negative numbers
assert remove_even([10, 15, 20, 25]) == [15, 25]  # Mixed even and odd

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_even([1,3,5,2]) == [1,3,5]
    assert remove_even([5,6,7]) == [5,7]
    assert remove_even([1,2,3,4]) == [1,3]
