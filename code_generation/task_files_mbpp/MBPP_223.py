# MBPP/223
### Completion
def is_majority(arr, n, x):
    # Find the first occurrence of x
    first_index = binary_search(arr, n, x, True)
    
    # If x is not present in the array
    if first_index == -1:
        return False
    
    # Find the last occurrence of x
    last_index = binary_search(arr, n, x, False)
    
    # Calculate the count of x
    count = last_index - first_index + 1
    
    # Check if count is greater than n/2
    return count > n // 2

def binary_search(arr, n, x, find_first):
    low, high = 0, n - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            result = mid
            if find_first:
                high = mid - 1  # Search for the first occurrence
            else:
                low = mid + 1   # Search for the last occurrence
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return result

# Test the function with the provided assertion
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
