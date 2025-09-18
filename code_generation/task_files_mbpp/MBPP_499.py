# MBPP/499
### Completion
def diameter_circle(radius):
    """Calculate the diameter of a circle given its radius."""
    return 2 * radius

# Test the function with the provided assertion
assert diameter_circle(10) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert diameter_circle(10)==20
    assert diameter_circle(40)==80
    assert diameter_circle(15)==30
