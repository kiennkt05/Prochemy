# MBPP/399
### Completion
def bitwise_xor(tuple1, tuple2):
    """
    Perform bitwise XOR operation on two tuples element-wise.

    Parameters:
    tuple1 (tuple): The first tuple of integers.
    tuple2 (tuple): The second tuple of integers.

    Returns:
    tuple: A new tuple containing the result of the bitwise XOR operation.
    """
    # Ensure both tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of the same length.")
    
    # Perform bitwise XOR for each pair of elements from the tuples
    result = tuple(a ^ b for a, b in zip(tuple1, tuple2))
    
    return result

# Test case
assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)

# Additional test cases can be added to verify the function
print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)
