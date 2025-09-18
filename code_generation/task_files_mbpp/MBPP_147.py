# MBPP/147
### Completion
def max_path_sum(triangle, row, col):
    # Start from the second to last row and move upwards
    for r in range(row - 1, -1, -1):
        for c in range(len(triangle[r])):
            # Update the current element to be itself plus the max of the two elements below it
            triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])
    
    # The top element now contains the maximum path sum
    return triangle[0][0]

# Test the function with the provided assertion
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
