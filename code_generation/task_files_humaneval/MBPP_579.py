# MBPP/579
### Completion
def find_dissimilar(tuple1, tuple2):
    """
    Find dissimilar elements in the given two tuples.

    Parameters:
    tuple1 (tuple): The first tuple of elements.
    tuple2 (tuple): The second tuple of elements.

    Returns:
    tuple: A tuple containing elements that are in either of the input tuples but not in both.
    """
    # Convert tuples to sets
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the symmetric difference
    dissimilar_elements = set1.symmetric_difference(set2)
    
    # Convert the result back to a tuple and return
    return tuple(dissimilar_elements)

# Test case
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
    assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)
    assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25)
