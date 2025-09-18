# MBPP/934
### Completion
def delannoy_num(m, n, memo=None):
    # Initialize memoization dictionary on the first call
    if memo is None:
        memo = {}
    
    # Check if the result is already computed
    if (m, n) in memo:
        return memo[(m, n)]
    
    # Base cases
    if m == 0 and n == 0:
        return 1
    if m == 0 or n == 0:
        return 1
    
    # Recursive calculation of Delannoy number
    result = (delannoy_num(m - 1, n, memo) +
              delannoy_num(m, n - 1, memo) +
              delannoy_num(m - 1, n - 1, memo))
    
    # Store the result in the memoization dictionary
    memo[(m, n)] = result
    return result

# Test case
assert delannoy_num(3, 4) == 129
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dealnnoy_num(3, 4) == 129
    assert dealnnoy_num(3, 3) == 63
    assert dealnnoy_num(4, 5) == 681
