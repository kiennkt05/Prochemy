# MBPP/673
### Completion
def convert(int_list):
    """
    Convert a list of integers into a single integer.

    Parameters:
    int_list (list of int): A list containing integers.

    Returns:
    int: A single integer formed by concatenating the integers in the list.
    """
    # Convert each integer to a string and join them
    concatenated_string = ''.join(map(str, int_list))
    # Convert the concatenated string back to an integer
    return int(concatenated_string)

# Test case
assert convert([1, 2, 3]) == 123
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert convert([1,2,3]) == 123
    assert convert([4,5,6]) == 456
    assert convert([7,8,9]) == 789
