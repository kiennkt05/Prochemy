# MBPP/763
### Completion
def find_Min_Diff(arr, n):
    # Sort the array
    arr = sorted(arr)
    
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # Iterate through the sorted array to find the minimum difference
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

# Test the function with the provided assertion
assert find_Min_Diff((1, 5, 3, 19, 18, 25), 6) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min_Diff((1,5,3,19,18,25),6) == 1
    assert find_Min_Diff((4,3,2,6),4) == 1
    assert find_Min_Diff((30,5,20,9),4) == 4
