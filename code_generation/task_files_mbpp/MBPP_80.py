# MBPP/80
### Completion
def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) / 6

# Test the function with the provided assertion
assert tetrahedral_number(5) == 35.0

# You can also print the result to verify
print(tetrahedral_number(5))  # Output: 35.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tetrahedral_number(5) == 35.0
    assert tetrahedral_number(6) == 56.0
    assert tetrahedral_number(7) == 84.0
