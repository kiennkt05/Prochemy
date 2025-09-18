# MBPP/101
### Completion
def kth_element(arr, n, k):
    # Sort the array
    arr.sort()
    # Return the k-1 index element (k is 1-based index)
    return arr[k - 1]

# Test the function with the provided assertion
assert kth_element([12, 3, 5, 7, 19], 5, 2) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert kth_element([12,3,5,7,19], 5, 2) == 3
    assert kth_element([17,24,8,23], 4, 3) == 8
    assert kth_element([16,21,25,36,4], 5, 4) == 36
