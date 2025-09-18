# MBPP/856
### Completion
def find_Min_Swaps(arr, n):
    # Initialize the count of swaps
    swap_count = 0
    # Count of zeros encountered so far
    count_zeros = 0
    
    # Iterate through the array
    for i in range(n):
        if arr[i] == 0:
            # Increment the count of zeros
            count_zeros += 1
        else:
            # For each 1, add the number of zeros encountered so far to swap_count
            swap_count += count_zeros
            
    return swap_count

# Test case
assert find_Min_Swaps([1, 0, 1, 0], 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min_Swaps([1,0,1,0],4) == 3
    assert find_Min_Swaps([0,1,0],3) == 1
    assert find_Min_Swaps([0,0,1,1,0],5) == 2
