# MBPP/769
### Completion
def Diff(list1, list2):
    """
    Returns the difference between two lists.
    
    The difference is defined as the elements that are in list1 but not in list2.
    
    Parameters:
    list1 (list): The first list from which to find the difference.
    list2 (list): The second list to compare against.
    
    Returns:
    list: A list containing elements from list1 that are not in list2.
    """
    # Using list comprehension to filter out elements in list1 that are not in list2
    return [item for item in list1 if item not in list2]

# Test case
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]
