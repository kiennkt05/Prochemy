# MBPP/384
### Completion
def frequency_of_smallest(n, arr):
    if not arr:
        return 0  # Return 0 if the array is empty
    
    smallest_value = min(arr)  # Find the smallest value in the array
    frequency = arr.count(smallest_value)  # Count the frequency of the smallest value
    
    return frequency

# Test the function with the provided assertion
assert frequency_of_smallest(5, [1, 2, 3, 4, 3]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency_Of_Smallest(5,[1,2,3,4,3]) == 1
    assert frequency_Of_Smallest(7,[3,1,2,5,6,2,3]) == 1
    assert frequency_Of_Smallest(7,[3,3,6,3,7,4,9]) == 3
