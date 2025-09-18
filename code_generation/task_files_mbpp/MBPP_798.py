# MBPP/798
### Completion
def _sum(array):
    return sum(array)

# Test the function
assert _sum([1, 2, 3]) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert _sum([1, 2, 3]) == 6
    assert _sum([15, 12, 13, 10]) == 50
    assert _sum([0, 1, 2]) == 3
