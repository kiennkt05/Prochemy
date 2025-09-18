# MBPP/444
### Completion
def trim_tuple(tuple_list, k):
    """
    Trims each tuple in the given list by the last k elements.
    
    Parameters:
    tuple_list (list of tuples): The list of tuples to be trimmed.
    k (int): The number of elements to trim from the end of each tuple.
    
    Returns:
    str: A string representation of the list of trimmed tuples.
    """
    trimmed_list = []
    
    for tup in tuple_list:
        # Trim the tuple by taking the last k elements
        if len(tup) > k:
            trimmed_tup = tup[-k:]  # Get the last k elements
        else:
            trimmed_tup = tup  # If tuple has fewer than k elements, take the whole tuple
        
        trimmed_list.append(trimmed_tup)
    
    return str(trimmed_list)

# Test the function with the provided test case
assert trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2) == '[(2,), (9,), (2,), (2,)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2) == '[(2,), (9,), (2,), (2,)]'
    assert trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 1) == '[(3, 2, 1), (4, 9, 2), (1, 2, 3), (8, 2, 1)]'
    assert trim_tuple([(7, 8, 4, 9), (11, 8, 12, 4),(4, 1, 7, 8), (3, 6, 9, 7)], 1) == '[(8, 4), (8, 12), (1, 7), (6, 9)]'
