# MBPP/401
### Completion
def add_nested_tuples(tuple1, tuple2):
    """
    Perform index-wise addition of elements in two nested tuples.

    Parameters:
    tuple1 (tuple): The first nested tuple containing tuples of integers.
    tuple2 (tuple): The second nested tuple containing tuples of integers.

    Returns:
    tuple: A new nested tuple containing the results of the index-wise addition.
    """
    # Using a tuple comprehension to add corresponding elements of the nested tuples
    return tuple(tuple(a + b for a, b in zip(inner1, inner2)) for inner1, inner2 in zip(tuple1, tuple2))

# Test case
assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))

# If the assertion passes, the function works as expected.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    assert add_nested_tuples(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    assert add_nested_tuples(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))
