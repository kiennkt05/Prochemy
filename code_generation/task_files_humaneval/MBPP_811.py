# MBPP/811
### Completion
def check_identical(list1, list2):
    """
    Check if two lists of tuples are identical.

    Parameters:
    list1 (list of tuples): The first list to compare.
    list2 (list of tuples): The second list to compare.

    Returns:
    bool: True if both lists are identical, False otherwise.
    """
    return list1 == list2

# Test cases
assert check_identical([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True
assert check_identical([(10, 4), (2, 5)], [(2, 5), (10, 4)]) == False
assert check_identical([(10, 4)], [(10, 4)]) == True
assert check_identical([], []) == True
assert check_identical([(1, 2)], [(1, 2), (3, 4)]) == False

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_identical([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True
    assert check_identical([(1, 2), (3, 7)], [(12, 14), (12, 45)]) == False
    assert check_identical([(2, 14), (12, 25)], [(2, 14), (12, 25)]) == True
