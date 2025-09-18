# MBPP/567
### Completion
def issort_list(lst):
    """
    Check if the given list is sorted in ascending order.

    Parameters:
    lst (list): The list to check.

    Returns:
    bool: True if the list is sorted, False otherwise.
    """
    # Iterate through the list and compare each element with the next
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False  # Found an element greater than the next one
    return True  # No elements were out of order

# Test case
assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) == True

# Additional test cases for verification
assert issort_list([1, 2, 3, 4]) == True  # Sorted list
assert issort_list([4, 3, 2, 1]) == False  # Not sorted
assert issort_list([1, 2, 2, 3]) == True  # Contains duplicates, still sorted
assert issort_list([]) == True  # Empty list is considered sorted
assert issort_list([1]) == True  # Single element list is sorted

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False
