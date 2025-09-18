# MBPP/147
### Completion
def max_path_sum(triangle, rows, cols):
    # Start from the second to last row and move upwards
    for row in range(rows - 2, -1, -1):
        for col in range(cols[row]):
            # Update the current element to be the sum of itself and the max of the two elements below it
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element now contains the maximum path sum
    return triangle[0][0]

# Test case
assert max_path_sum([[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2) == 14
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_path_sum([[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2) == 14
    assert max_path_sum([[13, 0, 0], [7, 4, 0], [2, 4, 6]], 2, 2) == 24 
    assert max_path_sum([[2, 0, 0], [11, 18, 0], [21, 25, 33]], 2, 2) == 53
