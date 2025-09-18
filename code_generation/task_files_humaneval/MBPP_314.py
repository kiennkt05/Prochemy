# MBPP/314
### Completion
def max_sum_rectangular_grid(grid, n):
    if n == 0:
        return 0
    if n == 1:
        return max(grid[0][0], grid[1][0])
    
    # Initialize the maximum sums for the first column
    prev_max = max(grid[0][0], grid[1][0])
    curr_max = 0
    
    for i in range(1, n):
        # Calculate the maximum sum for the current column
        take_first_row = grid[0][i] + (prev_max if i > 1 else 0)
        take_second_row = grid[1][i] + (prev_max if i > 1 else 0)
        
        # Update current max
        curr_max = max(prev_max, take_first_row, take_second_row)
        
        # Move to the next column
        prev_max = curr_max
    
    return curr_max

# Test case
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
