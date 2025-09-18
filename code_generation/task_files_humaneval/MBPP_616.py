# MBPP/616
### Completion
def tuple_modulo(tuple1, tuple2):
    """
    Perform the modulo operation on corresponding elements of two tuples.

    Parameters:
    tuple1 (tuple): The first tuple containing integers.
    tuple2 (tuple): The second tuple containing integers.

    Returns:
    tuple: A new tuple containing the results of the modulo operations.
    """
    # Ensure both tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of the same length.")
    
    # Perform modulo operation on corresponding elements
    result = tuple(a % b for a, b in zip(tuple1, tuple2))
    
    return result

# Test case
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)
