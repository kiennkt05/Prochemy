# MBPP/562
### Completion
def Find_Max_Length(sublists):
    """
    This function finds the maximum length of sublists within a list of lists.
    
    Parameters:
    sublists (list of list): A list containing sublists.
    
    Returns:
    int: The maximum length of the sublists.
    """
    # Initialize the maximum length to 0
    max_length = 0
    
    # Iterate through each sublist
    for sublist in sublists:
        # Update max_length if the current sublist is longer
        max_length = max(max_length, len(sublist))
    
    return max_length

# Test case
assert Find_Max_Length([[1], [1, 4], [5, 6, 7, 8]]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
    assert Find_Max_Length([[0,1],[2,2,],[3,2,1]]) == 3
    assert Find_Max_Length([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5
