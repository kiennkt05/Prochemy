# MBPP/81
### Completion
def zip_tuples(tuple1, tuple2):
    """
    Zips two tuples together, creating a list of tuples with all combinations
    of elements from the first tuple and the second tuple.

    Parameters:
    tuple1 (tuple): The first tuple.
    tuple2 (tuple): The second tuple.

    Returns:
    list: A list of tuples containing all combinations of elements from the two tuples.
    """
    result = []
    for item1 in tuple1:
        for item2 in tuple2:
            result.append((item1, item2))
    return result

# Test case
assert zip_tuples((7, 8, 4, 5, 9, 10), (1, 5, 6)) == [(7, 1), (7, 5), (7, 6), 
                                                      (8, 1), (8, 5), (8, 6), 
                                                      (4, 1), (4, 5), (4, 6), 
                                                      (5, 1), (5, 5), (5, 6), 
                                                      (9, 1), (9, 5), (9, 6), 
                                                      (10, 1), (10, 5), (10, 6)]

print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert zip_tuples((7, 8, 4, 5, 9, 10),(1, 5, 6) ) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
    assert zip_tuples((8, 9, 5, 6, 10, 11),(2, 6, 7) ) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]
    assert zip_tuples((9, 10, 6, 7, 11, 12),(3, 7, 8) ) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]
