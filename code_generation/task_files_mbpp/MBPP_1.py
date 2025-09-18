# MBPP/1
### Completion
def min_cost(cost, m, n):
    # Create a 2D array to store the minimum cost to reach each cell
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize the starting point
    dp[0][0] = cost[0][0]
    
    # Fill the first row
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    
    # Fill the first column
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    
    # Fill the rest of the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = cost[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    
    # The minimum cost to reach (m, n)
    return dp[m][n]

# Example usage
assert min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8
    assert min_cost([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2) == 12
    assert min_cost([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2) == 16
