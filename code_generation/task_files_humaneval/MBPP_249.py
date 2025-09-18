# MBPP/249
### Completion
def intersection_array(arr1, arr2):
    """
    Find the intersection of two arrays.

    Parameters:
    arr1 (list): The first array.
    arr2 (list): The second array.

    Returns:
    list: A list containing the intersection of arr1 and arr2.
    """
    # Use a lambda function to filter elements in arr1 that are also in arr2
    intersect = list(filter(lambda x: x in arr2, arr1))
    
    # Remove duplicates by converting to a set and back to a list
    return list(set(intersect))

# Test case
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]
