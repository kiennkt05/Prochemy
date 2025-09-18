# MBPP/354
### Completion
def tn_ap(a, d, n):
    return a + (n - 1) * d

# Test the function with the provided assertion
assert tn_ap(1, 5, 2) == 9
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tn_ap(1,5,2)==9
    assert tn_ap(2,6,4)==22
    assert tn_ap(1,4,5)==16
