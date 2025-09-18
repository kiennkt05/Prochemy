# MBPP/404
### Completion
def minimum(a, b):
    """Return the minimum of two numbers."""
    return a if a < b else b

# Test the function
assert minimum(1, 2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert minimum(1,2) == 1
    assert minimum(-5,-4) == -5
    assert minimum(0,0) == 0
