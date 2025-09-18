# MBPP/197
### Completion
def find_exponentio(tuple1, tuple2):
    return tuple(a ** b for a, b in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
    assert find_exponentio((11, 5, 6, 7), (6, 7, 8, 6)) == (1771561, 78125, 1679616, 117649)
    assert find_exponentio((12, 6, 7, 8), (7, 8, 9, 7)) == (35831808, 1679616, 40353607, 2097152)
