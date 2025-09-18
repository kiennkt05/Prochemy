# MBPP/320
### Completion
def sum_difference(n):
    # Calculate the squared sum
    sum_n = n * (n + 1) // 2
    squared_sum = sum_n ** 2
    
    # Calculate the sum of squares
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    # Calculate the difference
    difference = squared_sum - sum_of_squares
    
    return difference

# Test the function with the provided assertion
assert sum_difference(12) == 5434
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_difference(12)==5434
    assert sum_difference(20)==41230
    assert sum_difference(54)==2151270
