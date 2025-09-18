# MBPP/314
### Completion
def max_sum_rectangular_grid(grid, n):
    if n == 0:
        return 0
    if n == 1:
        return max(grid[0][0], grid[1][0])
    
    # Create a dp array to store the maximum sums
    dp = [0] * n
    
    # Base cases
    dp[0] = max(grid[0][0], grid[1][0])
    if n > 1:
        dp[1] = max(grid[0][0] + grid[1][1], grid[1][0] + grid[0][1], grid[0][1], grid[1][1])
    
    # Fill the dp array
    for i in range(2, n):
        dp[i] = max(dp[i-1], 
                     grid[0][i] + dp[i-2], 
                     grid[1][i] + dp[i-2])
    
    return dp[n-1]

# Test the function with the provided assertion
assert max_sum_rectangular_grid([[1, 4, 5], [2, 0, 0]], 3) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_rectangular_grid([ [1, 4, 5], [2, 0, 0 ] ], 3) == 7
    assert max_sum_rectangular_grid([ [ 1, 2, 3, 4, 5], [ 6, 7, 8, 9, 10] ], 5) == 24
    assert max_sum_rectangular_grid([ [7, 9, 11, 15, 19], [21, 25, 28, 31, 32] ], 5) == 81
