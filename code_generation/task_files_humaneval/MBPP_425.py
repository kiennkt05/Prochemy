# MBPP/425
### Completion
def count_element_in_list(sublists, element):
    """
    Count the number of sublists that contain a specific element.

    Parameters:
    sublists (list of list): A list containing sublists.
    element: The element to search for in the sublists.

    Returns:
    int: The count of sublists containing the element.
    """
    count = 0  # Initialize count of sublists containing the element
    
    # Iterate through each sublist
    for sublist in sublists:
        # Check if the element is in the current sublist
        if element in sublist:
            count += 1  # Increment count if element is found
    
    return count  # Return the final count

# Test case
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1
