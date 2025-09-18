# MBPP/310
### Completion
def string_to_tuple(s):
    """
    Convert a given string to a tuple of its characters.

    Parameters:
    s (str): The input string to be converted.

    Returns:
    tuple: A tuple containing each character of the string.
    """
    return tuple(s)

# Test case
assert string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# Additional test cases for verification
assert string_to_tuple("") == ()  # Empty string should return an empty tuple
assert string_to_tuple("abc") == ('a', 'b', 'c')  # Simple string
assert string_to_tuple("123") == ('1', '2', '3')  # Numeric string
assert string_to_tuple("!@#") == ('!', '@', '#')  # Special characters

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
    assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')
