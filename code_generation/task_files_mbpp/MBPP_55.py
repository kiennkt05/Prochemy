# MBPP/55
### Completion
def tn_gp(a, r, t):
    return a * (r ** (t - 1))

# Test the function with the provided assertion
assert tn_gp(1, 5, 2) == 16
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tn_gp(1,5,2)==16
    assert tn_gp(1,5,4)==256
    assert tn_gp(2,6,3)==486
