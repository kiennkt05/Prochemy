# MBPP/292
### Completion
def find(a, b):
    return a // b

# Test the function with the provided assertion
assert find(10, 3) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find(10,3) == 3
    assert find(4,2) == 2
    assert find(20,5) == 4
