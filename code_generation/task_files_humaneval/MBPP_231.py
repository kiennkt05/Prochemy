# MBPP/231
### Completion
def max_sum(triangle):
    """
    Calculate the maximum sum from top to bottom in a given right triangle of numbers.

    :param triangle: List of lists representing the triangle of numbers
    :return: Maximum sum from top to bottom
    """
    # Start from the second to last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current element to be itself plus the maximum of the two elements below it
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element now contains the maximum sum
    return triangle[0][0]

# Test case
assert max_sum([[1], [2, 1], [3, 3, 2]]) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum([[1], [2,1], [3,3,2]], 3) == 6
    assert max_sum([[1], [1, 2], [4, 1, 12]], 3) == 15 
    assert max_sum([[2], [3,2], [13,23,12]], 3) == 28
