# MBPP/921
### Completion
def chunk_tuples(input_tuple, n):
    # Use a list comprehension to create chunks of size n
    return [input_tuple[i:i + n] for i in range(0, len(input_tuple), n)]

# Test the function with the provided assertion
assert chunk_tuples((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert chunk_tuples((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
    assert chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 2) == [(1, 2), (3, 4), (5, 6), (7, 8), (9,)]
    assert chunk_tuples((11, 14, 16, 17, 19, 21, 22, 25), 4) == [(11, 14, 16, 17), (19, 21, 22, 25)]
