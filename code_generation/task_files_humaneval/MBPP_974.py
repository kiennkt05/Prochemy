# MBPP/974
### Completion
def min_sum_path(triangle):
    # Start from the second to last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current element with the minimum path sum
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element now contains the minimum path sum
    return triangle[0][0]

# Test case
assert min_sum_path([[2], [3, 9], [1, 6, 7]]) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_sum_path([[ 2 ], [3, 9 ], [1, 6, 7 ]]) == 6
    assert min_sum_path([[ 2 ], [3, 7 ], [8, 5, 6 ]]) == 10 
    assert min_sum_path([[ 3 ], [6, 4 ], [5, 2, 7 ]]) == 9
