# MBPP/815
### Completion
def sort_by_dnf(arr, n):
    """
    Sorts an array consisting of 0s, 1s, and 2s using the Dutch National Flag algorithm.
    
    Parameters:
    arr (list): The input array containing only 0s, 1s, and 2s.
    n (int): The length of the array.
    
    Returns:
    list: The sorted array.
    """
    low, mid, high = 0, 0, n - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Swap 0 to the low position
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1  # Move past 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]  # Swap 2 to the high position
            high -= 1
    
    return arr

# Test case
assert sort_by_dnf([1, 2, 0, 1, 0, 1, 2, 1, 1], 9) == [0, 0, 1, 1, 1, 1, 1, 2, 2]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_by_dnf([1,2,0,1,0,1,2,1,1], 9) == [0, 0, 1, 1, 1, 1, 1, 2, 2]
    assert sort_by_dnf([1,0,0,1,2,1,2,2,1,0], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
    assert sort_by_dnf([2,2,1,0,0,0,1,1,2,1], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
