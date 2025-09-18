# MBPP/70
### Completion
def get_equal(tuples_list, length):
    # Check if all tuples have the specified length
    if all(len(tup) == length for tup in tuples_list):
        return 'All tuples have same length'
    else:
        return 'Not all tuples have the same length'

# Example usage
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
