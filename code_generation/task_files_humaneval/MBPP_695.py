# MBPP/695
### Completion
def check_greater(tuple1, tuple2):
    """
    Check if each element of the second tuple is greater than its corresponding element in the first tuple.

    Parameters:
    tuple1 (tuple): The first tuple containing numeric values.
    tuple2 (tuple): The second tuple containing numeric values.

    Returns:
    bool: True if each element in tuple2 is greater than the corresponding element in tuple1, False otherwise.
    """
    # Check if both tuples have the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must have the same length.")
    
    # Compare each element of the second tuple with the corresponding element of the first tuple
    return all(b > a for a, b in zip(tuple1, tuple2))

# Test case
assert check_greater((10, 4, 5), (13, 5, 18)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_greater((10, 4, 5), (13, 5, 18)) == True
    assert check_greater((1, 2, 3), (2, 1, 4)) == False
    assert check_greater((4, 5, 6), (5, 6, 7)) == True
