# MBPP/291
### Completion
def count_no_of_ways(n, k):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k
    
    # Dynamic programming array
    dp = [0] * (n + 1)
    
    # Initializing base cases
    dp[1] = k
    dp[2] = k * k
    
    # Fill the dp array for the rest of the posts
    for i in range(3, n + 1):
        dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
    
    return dp[n]

# Test case
assert count_no_of_ways(2, 4) == 16
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228
