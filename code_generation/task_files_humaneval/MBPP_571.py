# MBPP/571
### Completion
def max_sum_pair_diff_lessthan_K(arr, n, k):
    # Sort the array to facilitate pairing
    arr.sort()
    
    total_sum = 0
    i = 0
    
    # Iterate through the array
    while i < n - 1:
        # Check if the difference between current and next element is less than k
        if abs(arr[i] - arr[i + 1]) < k:
            # If so, form a pair and add their sum to total_sum
            total_sum += arr[i] + arr[i + 1]
            # Move to the next pair (skip the next element)
            i += 2
        else:
            # If not, just move to the next element
            i += 1
            
    return total_sum

# Test case
assert max_sum_pair_diff_lessthan_K([3, 5, 10, 15, 17, 12, 9], 7, 4) == 62
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_pair_diff_lessthan_K([3, 5, 10, 15, 17, 12, 9], 7, 4) == 62
    assert max_sum_pair_diff_lessthan_K([5, 15, 10, 300], 4, 12) == 25
    assert max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5, 6], 6, 6) == 21
