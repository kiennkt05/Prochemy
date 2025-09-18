# MBPP/1
### Completion
def min_cost(cost, m, n):
    # Get the number of rows and columns
    rows = len(cost)
    cols = len(cost[0]) if rows > 0 else 0
    
    # Create a 2D list to store the minimum cost to reach each cell
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Initialize the starting point
    dp[0][0] = cost[0][0]
    
    # Fill the first row (only can come from the left)
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    
    # Fill the first column (only can come from above)
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    
    # Fill the rest of the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = cost[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    
    # The minimum cost to reach (m, n)
    return dp[m][n]

# Test case
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
