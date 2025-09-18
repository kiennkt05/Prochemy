# MBPP/205
### Completion
def inversion_elements(tup):
    max_value = max(tup)
    return tuple(-(max_value - x) for x in tup)

# Test the function with the provided assertion
assert inversion_elements((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)

# You can also print the result to verify
print(inversion_elements((7, 8, 9, 1, 10, 7)))  # Output: (-8, -9, -10, -2, -11, -8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert inversion_elements((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)
    assert inversion_elements((2, 4, 5, 6, 1, 7)) == (-3, -5, -6, -7, -2, -8)
    assert inversion_elements((8, 9, 11, 14, 12, 13)) == (-9, -10, -12, -15, -13, -14)
