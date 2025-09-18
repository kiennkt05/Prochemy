# MBPP/751
### Completion
def check_min_heap(arr, index):
    n = len(arr)
    
    # Calculate the left and right child indices
    left = 2 * index + 1
    right = 2 * index + 2
    
    # Check if the current index is a valid index
    if index >= n:
        return True
    
    # Check the left child
    if left < n and arr[left] < arr[index]:
        return False
    
    # Check the right child
    if right < n and arr[right] < arr[index]:
        return False
    
    # Recursively check the left and right subtrees
    return check_min_heap(arr, left) and check_min_heap(arr, right)

# Test the function with the provided assertion
assert check_min_heap([1, 2, 3, 4, 5, 6], 0) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6], 0) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15], 0) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15], 0) == False
