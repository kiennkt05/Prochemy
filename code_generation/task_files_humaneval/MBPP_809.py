# MBPP/809
### Completion
def check_smaller(tuple1, tuple2):
    """
    Check if each element of the second tuple is smaller than its corresponding element in the first tuple.

    Parameters:
    tuple1 (tuple): The first tuple containing comparison values.
    tuple2 (tuple): The second tuple containing values to be compared.

    Returns:
    bool: True if all elements in tuple2 are smaller than their corresponding elements in tuple1, False otherwise.
    """
    # Check if both tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of the same length.")
    
    # Compare each element of the second tuple with the corresponding element in the first tuple
    for a, b in zip(tuple1, tuple2):
        if b >= a:
            return False
    return True

# Test case
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_smaller((1, 2, 3), (2, 3, 4)) == False
    assert check_smaller((4, 5, 6), (3, 4, 5)) == True
    assert check_smaller((11, 12, 13), (10, 11, 12)) == True
