# MBPP/26
### Completion
def check_k_elements(tuple_list, k):
    """
    Check if all tuples in the given list have exactly k elements.

    Parameters:
    tuple_list (list of tuples): The list of tuples to check.
    k (int): The number of elements each tuple should have.

    Returns:
    bool: True if all tuples have exactly k elements, False otherwise.
    """
    for tup in tuple_list:
        if len(tup) != k:
            return False
    return True

# Test case
assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True
    assert check_k_elements([(7, 7, 7), (7, 7)], 7) == True
    assert check_k_elements([(9, 9), (9, 9, 9, 9)], 7) == False
