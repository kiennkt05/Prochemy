# MBPP/371
### Completion
def smallest_missing(arr, low, high):
    # Initialize the expected value to the lower bound
    expected = low
    
    # Iterate through the array
    for i in range(low, high + 1):
        # If the current element matches the expected value
        if i < len(arr) and arr[i] == expected:
            expected += 1  # Move to the next expected value
        else:
            # If the current index is out of bounds or the value does not match
            return expected  # The smallest missing element is found
    
    # If all elements are present, return the next expected value
    return expected

# Test case
assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
    assert smallest_missing([0, 1, 2, 6, 9, 11, 15], 0, 6) == 3
    assert smallest_missing([1, 2, 3, 4, 6, 9, 11, 15], 0, 7) == 0
