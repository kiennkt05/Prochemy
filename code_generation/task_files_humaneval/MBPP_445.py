# MBPP/445
### Completion
def index_multiplication(tuple1, tuple2):
    """
    Perform index-wise multiplication of elements in two tuples.

    Parameters:
    tuple1 (tuple): The first tuple containing pairs of numbers.
    tuple2 (tuple): The second tuple containing pairs of numbers.

    Returns:
    tuple: A new tuple containing the results of index-wise multiplication.
    """
    # Using a tuple comprehension to multiply corresponding elements
    result = tuple((a * b for a, b in zip(pair1, pair2)) for pair1, pair2 in zip(tuple1, tuple2))
    return result

# Test case
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))

# If the assertion passes, the function works as expected.
print("Function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))
