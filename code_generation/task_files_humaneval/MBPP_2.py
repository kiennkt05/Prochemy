# MBPP/2
### Completion
def similar_elements(tuple1, tuple2):
    """
    Find the similar elements from two given tuples.

    Parameters:
    tuple1 (tuple): The first tuple containing elements.
    tuple2 (tuple): The second tuple containing elements.

    Returns:
    tuple: A tuple containing the elements that are present in both input tuples.
    """
    # Convert tuples to sets to find common elements
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the intersection of both sets
    common_elements = set1.intersection(set2)
    
    # Convert the result back to a sorted tuple
    return tuple(sorted(common_elements))

# Test the function with the provided test case
assert similar_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)

# Additional test cases
assert similar_elements((1, 2, 3), (4, 5, 6)) == ()
assert similar_elements((1, 2, 3), (3, 2, 1)) == (1, 2, 3)
assert similar_elements((), ()) == ()
assert similar_elements((1, 2, 3), ()) == ()
assert similar_elements((), (1, 2, 3)) == ()

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)
    assert similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)
    assert similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)
