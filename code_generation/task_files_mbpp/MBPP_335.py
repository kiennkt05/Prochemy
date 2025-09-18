# MBPP/335
### Completion
def ap_sum(a, n, d):
    # Calculate the last term
    l = a + (n - 1) * d
    # Calculate the sum using the formula
    return (n / 2) * (a + l)

# Test the function with the provided assertion
assert ap_sum(1, 5, 2) == 25
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ap_sum(1,5,2)==25
    assert ap_sum(2,6,4)==72
    assert ap_sum(1,4,5)==34
