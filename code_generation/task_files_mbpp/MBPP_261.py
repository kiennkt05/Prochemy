# MBPP/261
### Completion
def division_elements(tuple1, tuple2):
    # Perform element-wise division and return the result as a tuple
    return tuple(a // b for a, b in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert division_elements((10, 4, 6, 9), (5, 2, 3, 3)) == (2, 2, 2, 3)

# You can print the result to verify
print(division_elements((10, 4, 6, 9), (5, 2, 3, 3)))  # Output: (2, 2, 2, 3)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
    assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
    assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)
