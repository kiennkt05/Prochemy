# MBPP/255
### Completion
from itertools import combinations_with_replacement

def combinations_colors(colors, n):
    """
    Generate all combinations of specified length n from the given list of colors,
    allowing for repetitions.

    Parameters:
    colors (list): A list of color strings.
    n (int): The number of colors to choose.

    Returns:
    list: A list of tuples containing the combinations.
    """
    # Generate combinations with replacement
    return list(combinations_with_replacement(colors, n))

# Test case
assert combinations_colors(["Red", "Green", "Blue"], 1) == [('Red',), ('Green',), ('Blue',)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
    assert combinations_colors( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')]
