# MBPP/89
### Completion
def closest_num(n):
    return n - 1

# Test the function
assert closest_num(11) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11
