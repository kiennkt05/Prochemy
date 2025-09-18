# MBPP/616
### Completion
def tuple_modulo(tuple1, tuple2):
    return tuple(a % b for a, b in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)

# You can also print the result to verify
print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))  # Output: (0, 4, 5, 1)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)
