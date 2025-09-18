# MBPP/2
### Completion
def similar_elements(tuple1, tuple2):
    # Convert tuples to sets to find the intersection
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the intersection of both sets
    similar = set1.intersection(set2)
    
    # Return the result as a sorted tuple
    return tuple(sorted(similar))

# Test the function with the provided assertion
assert similar_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)
    assert similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)
    assert similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)
