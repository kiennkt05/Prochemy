# MBPP/934
### Completion
def delannoy_num(m, n):
    # Create a 2D array to store the Delannoy numbers
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = 1  # Only one way to reach any cell in the first column
    for j in range(n + 1):
        dp[0][j] = 1  # Only one way to reach any cell in the first row
    
    # Fill the dp table using the recursive relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]
    
    return dp[m][n]

# Test the function with the provided assertion
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
