# MBPP/231
### Completion
def max_sum(triangle, n):
    # Start from the second to last row and move upwards
    for row in range(n - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current element to be itself plus the max of the two elements below it
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element now contains the maximum sum
    return triangle[0][0]

# Test the function with the provided assertion
assert max_sum([[1], [2, 1], [3, 3, 2]], 3) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum([[1], [2,1], [3,3,2]], 3) == 6
    assert max_sum([[1], [1, 2], [4, 1, 12]], 3) == 15 
    assert max_sum([[2], [3,2], [13,23,12]], 3) == 28
