# MBPP/103
### Completion
def eulerian_num(n, m, memo=None):
    # Initialize memoization dictionary on the first call
    if memo is None:
        memo = {}
    
    # Check if the result is already computed
    if (n, m) in memo:
        return memo[(n, m)]
    
    # Base cases
    if m == 0:
        return 1
    if n == m:
        return 1
    if n == 0 or m < 0 or m > n:
        return 0
    
    # Recursive case
    result = (n - m) * eulerian_num(n - 1, m - 1, memo) + (m + 1) * eulerian_num(n - 1, m, memo)
    
    # Store the result in the memoization dictionary
    memo[(n, m)] = result
    return result

# Test case
assert eulerian_num(3, 1) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26
