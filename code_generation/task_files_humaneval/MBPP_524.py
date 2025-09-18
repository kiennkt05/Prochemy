# MBPP/524
### Completion
def max_sum_increasing_subsequence(arr, n):
    # Edge case: if the array is empty
    if n == 0:
        return 0
    
    # Initialize the max_sum array
    max_sum = arr[:]  # Start with the same values as arr
    
    # Build the max_sum array
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:  # Check if we can extend the increasing subsequence
                max_sum[i] = max(max_sum[i], max_sum[j] + arr[i])
    
    # The result is the maximum value in max_sum
    return max(max_sum)

# Test case
assert max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5], 7) == 106
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5], 7) == 106
    assert max_sum_increasing_subsequence([3, 4, 5, 10], 4) == 22
    assert max_sum_increasing_subsequence([10, 5, 4, 3], 4) == 10
