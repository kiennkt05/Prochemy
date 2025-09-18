# MBPP/721
### Completion
def maxAverageOfPath(matrix, n):
    # Initialize the maximum average
    max_average = float('-inf')

    def dfs(x, y, current_sum, steps):
        nonlocal max_average
        # If we reach the bottom-right corner
        if x == n - 1 and y == n - 1:
            # Calculate the average
            average = current_sum / steps
            max_average = max(max_average, average)
            return
        
        # Possible moves: right and down
        if x + 1 < n:  # Move down
            dfs(x + 1, y, current_sum + matrix[x + 1][y], steps + 1)
        if y + 1 < n:  # Move right
            dfs(x, y + 1, current_sum + matrix[x][y + 1], steps + 1)

    # Start DFS from the top-left corner
    dfs(0, 0, matrix[0][0], 1)
    
    return max_average

# Test case
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]], 3) == 5.2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]], 3) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]], 3) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]], 3) == 7.2 
