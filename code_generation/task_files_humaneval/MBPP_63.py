# MBPP/63
### Completion
def max_difference(tuples_list):
    """
    Function to find the maximum difference between pairs in a given list of tuples.
    
    Args:
    tuples_list (list of tuples): A list where each tuple contains two integers.
    
    Returns:
    int: The maximum difference between the first and second elements of the tuples.
    """
    max_diff = 0  # Initialize maximum difference
    
    # Iterate through each tuple in the list
    for a, b in tuples_list:
        # Calculate the absolute difference
        diff = abs(a - b)
        # Update max_diff if the current difference is greater
        if diff > max_diff:
            max_diff = diff
            
    return max_diff

# Test case
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
