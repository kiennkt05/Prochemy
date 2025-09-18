# MBPP/218
### Completion
def min_Operations(a, b):
    return abs(a - b) // 2

# Test the function with the provided assertion
assert min_Operations(2, 4) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Operations(2,4) == 1
    assert min_Operations(4,10) == 4
    assert min_Operations(1,4) == 3
