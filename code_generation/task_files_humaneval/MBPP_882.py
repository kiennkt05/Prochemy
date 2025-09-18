# MBPP/882
### Completion
def parallelogram_perimeter(a, b):
    """
    Calculate the perimeter of a parallelogram.

    Parameters:
    a (int or float): Length of one side of the parallelogram.
    b (int or float): Length of the adjacent side of the parallelogram.

    Returns:
    int or float: The perimeter of the parallelogram.
    """
    return 2 * (a + b)

# Test the function with the provided assertion
assert parallelogram_perimeter(10, 20) == 60  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parallelogram_perimeter(10,20)==400
    assert parallelogram_perimeter(15,20)==600
    assert parallelogram_perimeter(8,9)==144
