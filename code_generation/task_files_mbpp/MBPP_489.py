# MBPP/489
### Completion
def frequency_of_largest(n, arr):
    if not arr:
        return 0
    
    largest_value = max(arr)
    frequency = arr.count(largest_value)
    
    return frequency

# Test the function with the provided assertion
assert frequency_of_largest(5, [1, 2, 3, 4, 4]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency_Of_Largest(5,[1,2,3,4,4]) == 2
    assert frequency_Of_Largest(3,[5,6,5]) == 1
    assert frequency_Of_Largest(4,[2,7,7,7]) == 3
