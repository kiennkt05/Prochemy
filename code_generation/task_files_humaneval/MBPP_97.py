# MBPP/97
### Completion
def frequency_lists(list_of_lists):
    """
    Function to count the frequency of elements in a list of lists.
    
    Parameters:
    list_of_lists (list of list): A list containing multiple lists of integers.
    
    Returns:
    dict: A dictionary with elements as keys and their frequency counts as values.
    """
    frequency_count = {}
    
    # Flatten the list of lists
    for inner_list in list_of_lists:
        for item in inner_list:
            if item in frequency_count:
                frequency_count[item] += 1
            else:
                frequency_count[item] = 1
                
    return frequency_count

# Test case
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
    assert frequency_lists([[1,2,3,4],[5,6,7,8],[9,10,11,12]])=={1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1,10:1,11:1,12:1}
    assert frequency_lists([[20,30,40,17],[18,16,14,13],[10,20,30,40]])=={20:2,30:2,40:2,17: 1,18:1, 16: 1,14: 1,13: 1, 10: 1}
