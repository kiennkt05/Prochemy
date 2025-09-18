# MBPP/721
### Completion
def maxAverageOfPath(matrix, n):
    def dfs(x, y, current_sum, steps):
        # If we reach the bottom-right corner, calculate the average
        if x == n - 1 and y == n - 1:
            return (current_sum + matrix[x][y]) / (steps + 1)
        
        # Mark the current cell as visited
        visited.add((x, y))
        max_avg = float('-inf')
        
        # Explore the four possible directions (down, up, right, left)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                avg = dfs(nx, ny, current_sum + matrix[x][y], steps + 1)
                max_avg = max(max_avg, avg)
        
        # Unmark the current cell (backtrack)
        visited.remove((x, y))
        return max_avg

    visited = set()
    return dfs(0, 0, 0, 0)

# Test the function with the provided assertion
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
