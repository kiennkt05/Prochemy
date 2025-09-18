# MBPP/571
### Completion
def max_sum_pair_diff_lessthan_K(arr, n, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    max_sum = 0
    i = 0
    
    while i < len(arr) - 1:
        # Check if the absolute difference is less than k
        if abs(arr[i] - arr[i + 1]) < k:
            # If it is, we can form a pair
            max_sum += arr[i] + arr[i + 1]
            # Move to the next pair
            i += 2
        else:
            # If not, just move to the next element
            i += 1
            
    return max_sum

# Test the function with the provided assertion
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
