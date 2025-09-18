# MBPP/766
### Completion
def pair_wise(lst):
    """
    Generate a list of tuples containing pairs of consecutive items from the input list.

    Args:
    lst (list): A list of items.

    Returns:
    list: A list of tuples, where each tuple contains a pair of consecutive items.
    """
    # Initialize an empty list to store the pairs
    pairs = []
    
    # Iterate over the list using index to access consecutive items
    for i in range(len(lst) - 1):
        # Create a tuple of the current item and the next item
        pairs.append((lst[i], lst[i + 1]))
    
    return pairs

# Test the function with the provided test case
assert pair_wise([1, 1, 2, 3, 3, 4, 4, 5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

# If the assertion passes, the function works as expected.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    assert pair_wise([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]
    assert pair_wise([1,2,3,4,5,6,7,8,9,10])==[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
