# MBPP/261
### Completion
def division_elements(tuple1, tuple2):
    """
    Perform element-wise division of two tuples.

    Parameters:
    tuple1 (tuple): The first tuple containing numbers.
    tuple2 (tuple): The second tuple containing numbers.

    Returns:
    tuple: A new tuple containing the results of the division.
    """
    # Ensure both tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must be of the same length.")
    
    # Perform element-wise division
    result = []
    for a, b in zip(tuple1, tuple2):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result.append(a // b)  # Use integer division

    return tuple(result)

# Test case
assert division_elements((10, 4, 6, 9), (5, 2, 3, 3)) == (2, 2, 2, 3)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
    assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
    assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)
