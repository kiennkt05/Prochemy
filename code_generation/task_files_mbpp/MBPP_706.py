# MBPP/706
### Completion
def is_subset(arr1, n, arr2, m):
    # Convert the second array to a set for O(1) lookups
    set_arr2 = set(arr2)
    
    # Check if all elements of arr1 are in set_arr2
    for element in arr1:
        if element not in set_arr2:
            return False
    return True

# Test the function with the provided assertion
assert is_subset([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_subset([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4) == True
    assert is_subset([1, 2, 3, 4, 5, 6], 6, [1, 2, 4], 3) == True
    assert is_subset([10, 5, 2, 23, 19], 5, [19, 5, 3], 3) == False
