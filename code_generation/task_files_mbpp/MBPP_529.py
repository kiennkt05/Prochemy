# MBPP/529
### Completion
def jacobsthal_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, b + 2 * a
        return b

# Test the function with the provided assertion
assert jacobsthal_lucas(5) == 31
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert jacobsthal_lucas(5) == 31
    assert jacobsthal_lucas(2) == 5
    assert jacobsthal_lucas(4) == 17
