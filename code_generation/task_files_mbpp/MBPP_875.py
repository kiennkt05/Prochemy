# MBPP/875
### Completion
def min_difference(tuples):
    # Initialize min_diff to a large number
    min_diff = float('inf')
    
    # Iterate through each tuple
    for a, b in tuples:
        # Calculate the absolute difference
        diff = abs(a - b)
        # Update min_diff if the current difference is smaller
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

# Test the function with the provided assertion
assert min_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 1
    assert min_difference([(4, 6), (12, 8), (11, 4), (2, 13)]) == 2
    assert min_difference([(5, 17), (3, 9), (12, 5), (3, 24)]) == 6
