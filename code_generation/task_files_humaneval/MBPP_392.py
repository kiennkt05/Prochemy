# MBPP/392
### Completion
def get_max_sum(n, memo=None):
    # Initialize memoization dictionary on the first call
    if memo is None:
        memo = {}
    
    # Check if the result is already computed
    if n in memo:
        return memo[n]
    
    # Base case: if n is 0, the maximum sum is 0
    if n == 0:
        return 0
    
    # Recursive calculation
    max_sum = max(get_max_sum(n // 2, memo) + 
                   get_max_sum(n // 3, memo) + 
                   get_max_sum(n // 4, memo) + 
                   get_max_sum(n // 5, memo), n)
    
    # Store the computed result in the memoization dictionary
    memo[n] = max_sum
    return max_sum

# Test case
assert get_max_sum(60) == 106

# You can add more test cases to validate the function
print(get_max_sum(60))  # Output: 106
print(get_max_sum(0))   # Output: 0
print(get_max_sum(1))   # Output: 1
print(get_max_sum(10))  # Output: 12
print(get_max_sum(100)) # Output: 200
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2
