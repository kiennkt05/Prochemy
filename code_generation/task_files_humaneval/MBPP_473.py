# MBPP/473
### Completion
def tuple_intersection(list1, list2):
    """
    Find the intersection of tuples in two lists, irrespective of their order.
    
    Parameters:
    list1 (list of tuples): The first list of tuples.
    list2 (list of tuples): The second list of tuples.
    
    Returns:
    set: A set containing the tuples that are present in both lists.
    """
    # Normalize tuples by sorting their elements
    normalized_set1 = {tuple(sorted(t)) for t in list1}
    normalized_set2 = {tuple(sorted(t)) for t in list2}
    
    # Find the intersection of the two sets
    intersection = normalized_set1.intersection(normalized_set2)
    
    # Return the intersection as a set of tuples
    return intersection

# Test case
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}
