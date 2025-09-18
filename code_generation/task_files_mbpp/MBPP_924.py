# MBPP/924
### Completion
def max_of_two(a, b):
    """Return the maximum of two numbers."""
    return a if a > b else b

# Test the function
assert max_of_two(10, 20) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_of_two(10,20)==20
    assert max_of_two(19,15)==19
    assert max_of_two(-10,-20)==-10
