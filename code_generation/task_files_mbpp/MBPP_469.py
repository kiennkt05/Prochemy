# MBPP/469
### Completion
def max_profit(prices, k):
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # If k is greater than half the number of days, we can make as many transactions as we want
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
    
    # Create a DP table
    dp = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    
    return dp[k][n - 1]

# Test the function with the provided assertion
assert max_profit([1, 5, 2, 3, 7, 6, 4, 5], 3) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_profit([1, 5, 2, 3, 7, 6, 4, 5], 3) == 10
    assert max_profit([2, 4, 7, 5, 4, 3, 5], 2) == 7
    assert max_profit([10, 6, 8, 4, 2], 2) == 2
