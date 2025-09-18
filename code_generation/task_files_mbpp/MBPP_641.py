# MBPP/641
### Completion
def is_nonagonal(n):
    return n * (7 * n - 5) // 2

# Test the function with the provided assertion
assert is_nonagonal(10) == 325

# You can also print the result to verify
print(is_nonagonal(10))  # Output should be 325
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089
