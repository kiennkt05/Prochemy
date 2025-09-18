# MBPP/362
### Completion
def max_occurrences(lst):
    """
    Find the item with the maximum occurrences in a given list.

    Parameters:
    lst (list): A list of items (can be of any type).

    Returns:
    The item with the maximum occurrences. If there are multiple items
    with the same maximum occurrences, the first one encountered in the
    list will be returned.
    """
    # Dictionary to store the count of each item
    count_dict = {}
    
    # Count occurrences of each item in the list
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    # Variables to track the item with the maximum occurrences
    max_item = None
    max_count = 0
    
    # Find the item with the maximum occurrences
    for item, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_item = item
    
    return max_item

# Test case
assert max_occurrences([1, 2, 3, 1, 2, 3, 12, 4, 2]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_occurrences([1,2,3,1,2,3,12,4,2]) ==  2
    assert max_occurrences([1,2,6,7,0,1,0,1,0]) == 1,0
    assert max_occurrences([1,2,3,1,2,4,1]) == 1
