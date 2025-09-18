# MBPP/351
### Completion
def first_Element(arr, n, k):
    """
    Function to find the first element occurring k times in the given array.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The size of the array.
    k (int): The number of occurrences to check for.
    
    Returns:
    int or None: The first element that occurs k times, or None if no such element exists.
    """
    count_map = {}
    
    for element in arr:
        # Update the count of the current element
        if element in count_map:
            count_map[element] += 1
        else:
            count_map[element] = 1
        
        # Check if the current element has reached k occurrences
        if count_map[element] == k:
            return element
    
    # If no element found that occurs k times
    return None

# Test case
assert first_Element([0, 1, 2, 3, 4, 5], 6, 1) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Element([0,1,2,3,4,5],6,1) == 0
    assert first_Element([1,2,1,3,4],5,2) == 1
    assert first_Element([2,3,4,3,5,7,1,2,3,5],10,2) == 2
