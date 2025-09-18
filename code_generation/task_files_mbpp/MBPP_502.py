# MBPP/502
### Completion
def find(a, b):
    return a % b

# Test the function with the provided assertion
assert find(3, 3) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find(3,3) == 0
    assert find(10,3) == 1
    assert find(16,5) == 1
