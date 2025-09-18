# MBPP/875
### Completion
def min_difference(tuples):
    """
    This function takes a list of tuples and returns the minimum absolute difference
    between the two elements of each tuple.

    :param tuples: List of tuples, where each tuple contains two integers
    :return: Minimum absolute difference among the tuples
    """
    # Initialize a variable to store the minimum difference
    min_diff = float('inf')  # Start with a very large number

    # Iterate through each tuple in the list
    for a, b in tuples:
        # Calculate the absolute difference
        diff = abs(a - b)
        # Update the minimum difference if the current one is smaller
        if diff < min_diff:
            min_diff = diff

    return min_diff

# Test case
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
