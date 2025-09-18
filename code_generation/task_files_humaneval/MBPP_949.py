# MBPP/949
### Completion
def sort_list(tuples_list):
    """
    Sorts a list of tuples based on the total number of digits in each tuple.

    Args:
    tuples_list (list of tuples): A list containing tuples of integers.

    Returns:
    str: A string representation of the sorted list of tuples.
    """
    # Function to calculate the total number of digits in a tuple
    def total_digits(tup):
        return sum(len(str(abs(num))) for num in tup)

    # Sort the list of tuples based on the total number of digits
    sorted_list = sorted(tuples_list, key=total_digits)

    # Return the sorted list as a string
    return str(sorted_list)

# Test case
assert sort_list([(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]) == '[(1, 2), (12345,), (3, 4, 6, 723), (134, 234, 34)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_list([(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)] ) == '[(1, 2), (12345,), (3, 4, 6, 723), (134, 234, 34)]'
    assert sort_list([(3, 4, 8), (1, 2), (1234335,), (1345, 234, 334)] ) == '[(1, 2), (3, 4, 8), (1234335,), (1345, 234, 334)]'
    assert sort_list([(34, 4, 61, 723), (1, 2), (145,), (134, 23)] ) == '[(1, 2), (145,), (134, 23), (34, 4, 61, 723)]'
