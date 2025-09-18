# MBPP/514
### Completion
def sum_elements(tup):
    """Returns the summation of elements in the given tuple."""
    return sum(tup)

# Test the function with the provided assertion
assert sum_elements((7, 8, 9, 1, 10, 7)) == 42

# You can also test the function with other tuples
print(sum_elements((1, 2, 3)))  # Output: 6
print(sum_elements((0, 0, 0)))  # Output: 0
print(sum_elements((-1, -2, -3)))  # Output: -6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_elements((7, 8, 9, 1, 10, 7)) == 42
    assert sum_elements((1, 2, 3, 4, 5, 6)) == 21
    assert sum_elements((11, 12 ,13 ,45, 14)) == 95
