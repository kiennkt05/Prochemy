# MBPP/429
### Completion
def and_tuples(tuple1, tuple2):
    """
    Extracts the elementwise differences from two tuples.
    
    Parameters:
    tuple1 (tuple): The first tuple of numbers.
    tuple2 (tuple): The second tuple of numbers.
    
    Returns:
    tuple: A new tuple containing the elementwise differences.
    """
    # Ensure both tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of the same length.")
    
    # Calculate the elementwise differences
    result = tuple(a - b for a, b in zip(tuple1, tuple2))
    
    return result

# Test the function with the provided test case
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (5, 2, 3, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
