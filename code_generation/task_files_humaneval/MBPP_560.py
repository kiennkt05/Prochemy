# MBPP/560
### Completion
def union_elements(tuple1, tuple2):
    """
    This function takes two tuples as input and returns a tuple containing the union of their elements.
    
    Parameters:
    tuple1 (tuple): The first tuple of elements.
    tuple2 (tuple): The second tuple of elements.
    
    Returns:
    tuple: A tuple containing the union of elements from both input tuples.
    """
    # Convert tuples to sets to perform union operation
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Perform union of both sets
    union_set = set1.union(set2)
    
    # Convert the resulting set back to a tuple and return
    return tuple(union_set)

# Test case
assert union_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
    assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)
    assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)
