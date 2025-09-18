# MBPP/429
### Completion
def and_tuples(tuple1, tuple2):
    # Use a generator expression to create a new tuple with the elementwise minimum
    return tuple(min(a, b) for a, b in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
