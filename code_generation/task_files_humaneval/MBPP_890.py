# MBPP/890
### Completion
def find_Extra(arr1, arr2, n):
    """
    Find the index of the extra element in the sorted array arr1.
    
    Parameters:
    arr1 (list): The first sorted array with an extra element.
    arr2 (list): The second sorted array without the extra element.
    n (int): The length of arr2.
    
    Returns:
    int: The index of the extra element in arr1.
    """
    # Iterate through the elements of arr2
    for i in range(n):
        if arr1[i] != arr2[i]:
            return i  # Return the index of the extra element
    
    # If no mismatch found in the first n elements, the extra element is at the end
    return n  # The extra element is at the last index of arr1

# Test case
assert find_Extra([1, 2, 3, 4], [1, 2, 3], 3) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Extra([1,2,3,4],[1,2,3],3) == 3
    assert find_Extra([2,4,6,8,10],[2,4,6,8],4) == 4
    assert find_Extra([1,3,5,7,9,11],[1,3,5,7,9],5) == 5
