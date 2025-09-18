# MBPP/763
### Completion
def find_Min_Diff(arr, n):
    # Step 1: Sort the array
    sorted_arr = sorted(arr)
    
    # Step 2: Initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # Step 3: Calculate the differences between adjacent elements
    for i in range(n - 1):
        diff = sorted_arr[i + 1] - sorted_arr[i]
        # Update the minimum difference if the current difference is smaller
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

# Test case
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
