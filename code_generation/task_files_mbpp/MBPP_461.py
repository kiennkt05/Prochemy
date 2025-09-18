# MBPP/461
### Completion
def upper_ctr(s):
    return sum(1 for char in s if char.isupper())

# Test the function with the provided assertion
assert upper_ctr('PYthon') == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0
