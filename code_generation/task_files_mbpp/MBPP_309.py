# MBPP/309
### Completion
def maximum(a, b):
    """Return the maximum of two numbers."""
    return a if a > b else b

# Test the function
assert maximum(5, 10) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum(5,10) == 10
    assert maximum(-1,-2) == -1
    assert maximum(9,7) == 9
