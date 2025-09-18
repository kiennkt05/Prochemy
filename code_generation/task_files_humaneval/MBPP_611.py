# MBPP/611
### Completion
def max_of_nth(tuple_list, n):
    """
    Find the maximum value in the nth column of a list of tuples.

    Parameters:
    tuple_list (list of tuples): The list containing tuples.
    n (int): The index of the column to find the maximum value from.

    Returns:
    The maximum value in the nth column.
    """
    # Extract the nth column using a list comprehension
    nth_column = [t[n] for t in tuple_list]
    
    # Return the maximum value from the nth column
    return max(nth_column)

# Test case
assert max_of_nth([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_of_nth([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19
    assert max_of_nth([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 10
    assert max_of_nth([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 1) == 11
