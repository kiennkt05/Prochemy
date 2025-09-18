# MBPP/360
### Completion
def get_carol(n):
    return (2 ** (n + 1)) - 1

# Test the function with the provided assertion
assert get_carol(2) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_carol(2) == 7
    assert get_carol(4) == 223
    assert get_carol(5) == 959
