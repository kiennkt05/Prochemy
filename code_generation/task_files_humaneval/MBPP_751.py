# MBPP/751
### Completion
def check_min_heap(arr, index):
    n = len(arr)
    
    # Check if the current index is a valid index
    if index >= n:
        return True  # An empty subtree is a valid min-heap
    
    # Calculate the indices of the left and right children
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    
    # Check the left child
    if left_child_index < n and arr[index] > arr[left_child_index]:
        return False
    
    # Check the right child
    if right_child_index < n and arr[index] > arr[right_child_index]:
        return False
    
    # Recursively check the left and right subtrees
    return check_min_heap(arr, left_child_index) and check_min_heap(arr, right_child_index)

# Test case
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
