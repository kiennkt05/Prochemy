# MBPP/658
### Completion
from collections import Counter

def max_occurrences(lst):
    """
    Find the item with the maximum occurrences in the given list.
    
    Parameters:
    lst (list): A list of items (can be of any type that is hashable).
    
    Returns:
    The item with the maximum occurrences. If there are multiple items with the same maximum count,
    the first one encountered in the list will be returned.
    """
    # Count occurrences of each item in the list
    counts = Counter(lst)
    
    # Find the item with the maximum occurrences
    max_item = None
    max_count = 0
    
    for item, count in counts.items():
        if count > max_count:
            max_count = count
            max_item = item
            
    return max_item

# Test case
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2])==2
    assert max_occurrences([1, 3,5, 7,1, 3,13, 15, 17,5, 7,9,1, 11])==1
    assert max_occurrences([1, 2, 3,2, 4, 5,1, 1, 1])==1
