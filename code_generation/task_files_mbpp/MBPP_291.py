# MBPP/291
### Completion
def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k

    # dp[i] will store the number of ways to paint i posts
    dp = [0] * (n + 1)
    
    # Base cases
    dp[1] = k
    dp[2] = k * k

    for i in range(3, n + 1):
        # The recurrence relation:
        # dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])

    return dp[n]

# Test the function with the provided assertion
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
