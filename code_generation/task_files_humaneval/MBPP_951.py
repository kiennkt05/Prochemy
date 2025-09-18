# MBPP/951
### Completion
def max_similar_indices(list1, list2):
    """
    This function takes two lists of tuples and returns a new list of tuples
    where each tuple is the maximum of the tuples at the same index from both lists.
    
    If the first elements of the tuples are equal, the tuple from the first list is chosen.
    
    Parameters:
    list1 (list of tuples): The first list of tuples.
    list2 (list of tuples): The second list of tuples.
    
    Returns:
    list of tuples: A list containing the maximum tuples from both lists.
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the indices of the lists
    for i in range(len(list1)):
        # Compare the tuples at the same index
        if list1[i][0] >= list2[i][0]:
            result.append(list1[i])
        else:
            result.append(list2[i])
    
    return result

# Test case
assert max_similar_indices([(2, 4), (6, 7), (5, 1)], [(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_similar_indices([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
    assert max_similar_indices([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]
    assert max_similar_indices([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]
