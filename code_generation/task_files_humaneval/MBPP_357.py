# MBPP/357
### Completion
def find_max(tuples):
    """
    Find the maximum element from a list of tuples.

    Parameters:
    tuples (list of tuple): A list containing tuples of integers.

    Returns:
    int: The maximum integer found in all the tuples.
    """
    # Initialize max_value to a very small number
    max_value = float('-inf')
    
    # Iterate through each tuple in the list
    for tup in tuples:
        # Find the maximum in the current tuple
        current_max = max(tup)
        # Update the overall maximum if the current max is greater
        if current_max > max_value:
            max_value = current_max
            
    return max_value

# Test case
assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
    assert find_max([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
    assert find_max([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12
