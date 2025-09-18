# MBPP/418
### Completion
def Find_Max(list_of_lists):
    """
    This function finds the sublist with the maximum length from a list of lists.
    
    Parameters:
    list_of_lists (list of list): A list containing sublists.
    
    Returns:
    list: The sublist with the maximum length.
    """
    # Initialize a variable to keep track of the longest sublist
    max_length_sublist = []
    
    # Iterate through each sublist in the list of lists
    for sublist in list_of_lists:
        # Check if the current sublist is longer than the max_length_sublist
        if len(sublist) > len(max_length_sublist):
            max_length_sublist = sublist  # Update the longest sublist
    
    return max_length_sublist

# Test case
assert Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
