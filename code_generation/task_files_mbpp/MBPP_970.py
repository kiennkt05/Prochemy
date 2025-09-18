# MBPP/970
### Completion
def min_of_two(a, b):
    """Return the minimum of two numbers."""
    return a if a < b else b

# Test the function with the provided assertion
assert min_of_two(10, 20) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_of_two(10,20)==10
    assert min_of_two(19,15)==15
    assert min_of_two(-10,-20)==-20
