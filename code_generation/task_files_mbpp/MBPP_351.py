# MBPP/351
### Completion
def first_Element(arr, n, k):
    count = {}
    
    # Count occurrences of each element
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        
        # Check if the current element has occurred k times
        if count[num] == k:
            return num
    
    # If no element occurs k times, return None or an appropriate value
    return None

# Test the function with the provided assertion
assert first_Element([0, 1, 2, 3, 4, 5], 6, 1) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Element([0,1,2,3,4,5],6,1) == 0
    assert first_Element([1,2,1,3,4],5,2) == 1
    assert first_Element([2,3,4,3,5,7,1,2,3,5],10,2) == 2
