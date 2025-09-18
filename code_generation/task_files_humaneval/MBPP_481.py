# MBPP/481
### Completion
def is_subset_sum(set, n, sum):
    # Create a 2D array to store results of subproblems
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    
    # If sum is 0, then answer is True (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if set[i - 1] > j:
                dp[i][j] = dp[i - 1][j]  # Exclude the element
            else:
                # Include the element or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - set[i - 1]]

    return dp[n][sum]

# Test case
assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9) == True
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30) == False
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 15) == True
