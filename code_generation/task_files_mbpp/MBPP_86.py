# MBPP/86
### Completion
def centered_hexagonal_number(n):
    return 3 * n * (n - 1) + 1

# Test the function with the provided assertion
assert centered_hexagonal_number(10) == 271
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217
