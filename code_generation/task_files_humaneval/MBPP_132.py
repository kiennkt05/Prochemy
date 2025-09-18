# MBPP/132
### Completion
def tup_string(tup):
    """
    Convert a tuple of characters into a string.

    Parameters:
    tup (tuple): A tuple containing characters.

    Returns:
    str: A string formed by concatenating the characters in the tuple.
    """
    # Use join to concatenate the characters in the tuple into a single string
    return ''.join(tup)

# Test the function with the provided assertion
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"

# If the assertion passes, the function works as expected.
print("Assertion passed. The function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
    assert tup_string(('p','y','t','h','o','n'))==("python")
    assert tup_string(('p','r','o','g','r','a','m'))==("program")
