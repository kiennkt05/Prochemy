# MBPP/70
### Completion
def get_equal(tuples_list, expected_length):
    """
    Check if all tuples in the given list have the same length as expected_length.

    Parameters:
    tuples_list (list of tuples): A list containing tuples to check.
    expected_length (int): The length that each tuple should have.

    Returns:
    str: A message indicating whether all tuples have the same length.
    """
    # Check if all tuples have the expected length
    if all(len(tup) == expected_length for tup in tuples_list):
        return 'All tuples have same length'
    else:
        return 'Not all tuples have the same length'

# Test case
assert get_equal([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
    assert get_equal([(1, 2), (3, 4)], 2) == 'All tuples have same length'
