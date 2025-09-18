# MBPP/393
### Completion
def max_length_list(lists):
    """
    Find the list with the maximum length from a list of lists.

    Args:
    lists (list of list): A list containing multiple lists.

    Returns:
    tuple: A tuple containing the length of the longest list and the longest list itself.
    """
    # Use max with a lambda function to find the longest list
    longest_list = max(lists, key=lambda x: len(x))
    return (len(longest_list), longest_list)

# Test the function with the provided test case
assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])

# You can add more test cases to validate the function
print(max_length_list([[1], [2, 3], [4, 5, 6], [7]]))  # Expected output: (3, [4, 5, 6])
print(max_length_list([[], [1], [2, 3, 4], [5, 6]]))  # Expected output: (3, [2, 3, 4])
print(max_length_list([[1, 2], [3], [4, 5, 6, 7], [8]]))  # Expected output: (4, [4, 5, 6, 7])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(5,[1,2,3,4,5])
    assert max_length_list([[3,4,5],[6,7,8,9],[10,11,12]])==(4,[6,7,8,9])
