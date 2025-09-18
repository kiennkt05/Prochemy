# MBPP/560
### Completion
def union_elements(tuple1, tuple2):
    # Convert tuples to sets to find the union
    union_set = set(tuple1).union(set(tuple2))
    # Convert the set back to a sorted tuple
    return tuple(sorted(union_set))

# Test the function with the provided assertion
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
