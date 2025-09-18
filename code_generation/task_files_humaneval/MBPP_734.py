# MBPP/734
### Completion
def sum_Of_Subarray_Prod(arr, n):
    total_sum = 0
    
    # Iterate over all possible starting points of subarrays
    for start in range(n):
        product = 1
        
        # Iterate over all possible ending points of subarrays
        for end in range(start, n):
            product *= arr[end]  # Calculate the product of the current subarray
            total_sum += product  # Add the product to the total sum
            
    return total_sum

# Test case
assert sum_Of_Subarray_Prod([1, 2, 3], 3) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3],3) == 20
    assert sum_Of_Subarray_Prod([1,2],2) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4],4) == 84
