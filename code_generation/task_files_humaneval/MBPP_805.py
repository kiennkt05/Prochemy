# MBPP/805
### Completion
def max_sum_list(lists):
    """
    Find the list in a list of lists whose sum of elements is the highest.

    Parameters:
    lists (list of list of int): A list containing sublists of integers.

    Returns:
    list: The sublist with the highest sum of its elements.
    """
    max_sum = float('-inf')  # Initialize to negative infinity
    max_list = []  # This will hold the list with the maximum sum

    for sublist in lists:
        current_sum = sum(sublist)  # Calculate the sum of the current sublist
        if current_sum > max_sum:  # Check if the current sum is greater than the max sum
            max_sum = current_sum  # Update max sum
            max_list = sublist  # Update the list with the highest sum

    return max_list  # Return the list with the highest sum

# Test case
assert max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12] 
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10] 
    assert max_sum_list([[2,3,1]])==[2,3,1] 
