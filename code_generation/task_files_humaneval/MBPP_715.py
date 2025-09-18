# MBPP/715
### Completion
def str_to_tuple(s):
    """
    Convert a string of integers into a tuple of integers.

    Parameters:
    s (str): A string containing integers separated by commas.

    Returns:
    tuple: A tuple containing the integers.
    """
    # Split the string by commas and strip whitespace, then convert to integers
    int_list = [int(num.strip()) for num in s.split(',')]
    # Convert the list to a tuple and return it
    return tuple(int_list)

# Test case
assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)

# Additional test cases for verification
assert str_to_tuple("10, 20, 30") == (10, 20, 30)
assert str_to_tuple("  -1, 0, 1 ") == (-1, 0, 1)
assert str_to_tuple("100") == (100,)
assert str_to_tuple("") == ()  # Edge case: empty string should return an empty tuple

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)
    assert str_to_tuple("1, 2, 3, 4, 5") == (1, 2, 3, 4, 5)
    assert str_to_tuple("4, 6, 9, 11, 13, 14") == (4, 6, 9, 11, 13, 14)
