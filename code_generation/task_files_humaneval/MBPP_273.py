# MBPP/273
### Completion
def substract_elements(tuple1, tuple2):
    """
    Subtracts the elements of tuple2 from tuple1 at corresponding indices.

    Parameters:
    tuple1 (tuple): The first tuple from which elements will be subtracted.
    tuple2 (tuple): The second tuple whose elements will be subtracted from the first.

    Returns:
    tuple: A new tuple containing the results of the subtraction.
    """
    # Ensure both tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of the same length.")
    
    # Subtract elements of tuple2 from tuple1
    result = tuple(a - b for a, b in zip(tuple1, tuple2))
    
    return result

# Test case
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)

# You can add more test cases to validate the function further
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
    assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)
