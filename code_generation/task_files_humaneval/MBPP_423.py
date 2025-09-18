# MBPP/423
### Completion
def get_maxgold(gold_mine, rows, cols):
    # Create a DP table to store the maximum gold collected up to each cell
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Initialize the first row of the DP table
    for j in range(cols):
        dp[0][j] = gold_mine[0][j]
    
    # Fill the DP table
    for i in range(1, rows):
        for j in range(cols):
            # Gold collected from the cell directly above
            up = dp[i-1][j]
            # Gold collected from the left diagonal cell (if not out of bounds)
            left_diagonal = dp[i-1][j-1] if j > 0 else 0
            # Gold collected from the right diagonal cell (if not out of bounds)
            right_diagonal = dp[i-1][j+1] if j < cols - 1 else 0
            
            # Current cell's gold + max of the three possible previous cells
            dp[i][j] = gold_mine[i][j] + max(up, left_diagonal, right_diagonal)
    
    # The result is the maximum gold collected in the last row
    return max(dp[rows-1])

# Test the function with the provided test case
assert get_maxgold([[1, 3, 1, 5],
                     [2, 2, 4, 1],
                     [5, 0, 2, 3],
                     [0, 6, 1, 2]], 4, 4) == 16

print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_maxgold([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]],4,4)==16
    assert get_maxgold([[10,20],[30,40]],2,2)==70
    assert get_maxgold([[4,9],[3,7]],2,2)==13
