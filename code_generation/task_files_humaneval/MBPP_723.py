# MBPP/723
### Completion
def count_same_pair(list1, list2):
    """
    Count the number of positions where the elements of two lists are the same.

    Parameters:
    list1 (list): The first list of elements.
    list2 (list): The second list of elements.

    Returns:
    int: The count of same pairs in the two lists.
    """
    # Use map to compare elements of both lists and create a list of boolean values
    same_pairs = map(lambda x: x[0] == x[1], zip(list1, list2))
    
    # Sum the boolean values (True is 1, False is 0) to get the count of same pairs
    return sum(same_pairs)

# Test case
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
    assert count_same_pair([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==11
    assert count_same_pair([2, 4, -6, -9, 11, -12, 14, -5, 17],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==1
