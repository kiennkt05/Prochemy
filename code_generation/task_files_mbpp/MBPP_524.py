# MBPP/524
### Completion
def max_sum_increasing_subsequence(arr, n):
    # Create an array to store the maximum sum of increasing subsequence
    max_sum = [0] * n
    
    # Initialize the max_sum array with the values of the original array
    for i in range(n):
        max_sum[i] = arr[i]
    
    # Compute the maximum sum of increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and max_sum[i] < max_sum[j] + arr[i]:
                max_sum[i] = max_sum[j] + arr[i]
    
    # The result is the maximum value in max_sum array
    return max(max_sum)

# Test the function with the provided assertion
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
