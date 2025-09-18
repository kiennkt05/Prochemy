# MBPP/279
### Completion
def nth_decagonal(n):
    """Return the nth decagonal number."""
    return n * (4 * n - 3)

# Test the function with the provided assertion
assert nth_decagonal(3) == 27

# You can also print the result to verify
print(nth_decagonal(3))  # Output: 27
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370
