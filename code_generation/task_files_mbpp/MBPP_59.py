# MBPP/59
### Completion
def is_octagonal(n):
    return n * (3 * n - 2)

# Test the function with the provided assertion
assert is_octagonal(5) == 65

# You can also print the result to verify
print(is_octagonal(5))  # Output: 65
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645
