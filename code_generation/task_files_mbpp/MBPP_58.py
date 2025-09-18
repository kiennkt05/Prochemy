# MBPP/58
### Completion
def opposite_Signs(a, b):
    return (a < 0) != (b < 0)

# Test the function with the provided assertion
assert opposite_Signs(1, -2) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert opposite_Signs(1,-2) == True
    assert opposite_Signs(3,2) == False
    assert opposite_Signs(-10,-10) == False
