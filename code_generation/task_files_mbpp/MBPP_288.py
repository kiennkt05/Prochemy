# MBPP/288
### Completion
def modular_inverse(arr, n, p):
    count = 0
    for a in arr:
        if a % p == 1 or a % p == p - 1:
            count += 1
    return count

# Test the function with the provided assertion
assert modular_inverse([1, 6, 4, 5], 4, 7) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert modular_inverse([ 1, 6, 4, 5 ], 4, 7) == 2
    assert modular_inverse([1, 3, 8, 12, 12], 5, 13) == 3
    assert modular_inverse([2, 3, 4, 5], 4, 6) == 1
