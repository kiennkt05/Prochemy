# MBPP/888
### Completion
def substract_elements(t1, t2):
    """
    Subtracts elements of two nested tuples element-wise.

    Parameters:
    t1 (tuple): The first nested tuple.
    t2 (tuple): The second nested tuple.

    Returns:
    tuple: A new nested tuple containing the results of the subtraction.
    """
    # Using a tuple comprehension to iterate through the outer tuples
    result = tuple(
        tuple(a - b for a, b in zip(inner_t1, inner_t2))
        for inner_t1, inner_t2 in zip(t1, t2)
    )
    return result

# Test case
assert substract_elements(((1, 3), (4, 5), (2, 9), (1, 10)), 
                          ((6, 7), (3, 9), (1, 1), (7, 3))) == ((-5, -4), (1, -4), (1, 8), (-6, 7))

print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert substract_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((-5, -4), (1, -4), (1, 8), (-6, 7))
    assert substract_elements(((13, 4), (14, 6), (13, 10), (12, 11)), ((19, 8), (14, 10), (12, 2), (18, 4))) == ((-6, -4), (0, -4), (1, 8), (-6, 7))
    assert substract_elements(((19, 5), (18, 7), (19, 11), (17, 12)), ((12, 9), (17, 11), (13, 3), (19, 5))) == ((7, -4), (1, -4), (6, 8), (-2, 7))
