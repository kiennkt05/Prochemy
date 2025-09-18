# MBPP/116
### Completion
def tuple_to_int(tup):
    """
    Convert a tuple of positive integers into a single integer.

    Parameters:
    tup (tuple): A tuple containing positive integers.

    Returns:
    int: The integer formed by concatenating the integers in the tuple.
    """
    # Convert each integer in the tuple to a string and join them
    str_number = ''.join(map(str, tup))
    # Convert the concatenated string back to an integer
    return int(str_number)

# Test case
assert tuple_to_int((1, 2, 3)) == 123
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567
