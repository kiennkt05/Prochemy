# MBPP/23
### Completion
def maximum_Sum(list_of_lists):
    """
    This function takes a list of lists and returns the maximum sum of elements
    from any of the sublists.

    :param list_of_lists: List of lists containing numerical elements
    :return: Maximum sum of elements from any sublist
    """
    max_sum = float('-inf')  # Initialize to negative infinity to handle all negative numbers

    for sublist in list_of_lists:
        current_sum = sum(sublist)  # Calculate the sum of the current sublist
        if current_sum > max_sum:    # Update max_sum if current_sum is greater
            max_sum = current_sum

    return max_sum

# Test case
assert maximum_Sum([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == 33
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum_Sum([[1,2,3],[4,5,6],[10,11,12],[7,8,9]]) == 33
    assert maximum_Sum([[0,1,1],[1,1,2],[3,2,1]]) == 6
    assert maximum_Sum([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]]) == 19
