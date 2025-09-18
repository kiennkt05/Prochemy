# MBPP/363
### Completion
def add_K_element(tuples_list, k):
    """
    Adds the integer k to each element in each tuple of the given list of tuples.

    Parameters:
    tuples_list (list of tuples): A list containing tuples of integers.
    k (int): The integer to be added to each element of the tuples.

    Returns:
    list of tuples: A new list containing tuples with k added to each element.
    """
    # Create a new list to hold the modified tuples
    result = []
    
    # Iterate through each tuple in the input list
    for tup in tuples_list:
        # Create a new tuple with k added to each element
        new_tup = tuple(x + k for x in tup)
        # Append the new tuple to the result list
        result.append(new_tup)
    
    return result

# Test case
assert add_K_element([(1, 3, 4), (2, 4, 6), (3, 8, 1)], 4) == [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_K_element([(1, 3, 4), (2, 4, 6), (3, 8, 1)], 4) == [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
    assert add_K_element([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 8) == [(9, 10, 11), (12, 13, 14), (15, 16, 17)]
    assert add_K_element([(11, 12, 13), (14, 15, 16), (17, 18, 19)], 9) == [(20, 21, 22), (23, 24, 25), (26, 27, 28)]
