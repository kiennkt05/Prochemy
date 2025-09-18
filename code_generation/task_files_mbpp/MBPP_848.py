# MBPP/848
### Completion
def area_trapezium(a, b, h):
    return 0.5 * (a + b) * h

# Test the function with the provided assertion
assert area_trapezium(6, 9, 4) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert area_trapezium(6,9,4)==30
    assert area_trapezium(10,20,30)==450
    assert area_trapezium(15,25,35)==700
