# MBPP/93
### Completion
def power(a, b):
    return a ** b

# Test the function with the provided assertion
assert power(3, 4) == 81
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125
