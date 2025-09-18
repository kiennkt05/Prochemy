# MBPP/306
### Completion
def max_sum_increasing_subseq(arr, n, i, k):
    # Step 1: Calculate the maximum sum of increasing subsequence up to index i
    max_sum = [0] * (i + 1)
    
    for j in range(i + 1):
        max_sum[j] = arr[j]
        for l in range(j):
            if arr[l] < arr[j]:
                max_sum[j] = max(max_sum[j], max_sum[l] + arr[j])
    
    # Step 2: Find the maximum sum up to index i
    max_sum_up_to_i = max(max_sum[:i + 1])
    
    # Step 3: Check if we can include arr[k] in the subsequence
    if arr[k] > arr[i]:  # arr[k] must be greater than the last element in the subsequence
        return max_sum_up_to_i + arr[k]
    
    return max_sum_up_to_i

# Test the function with the provided assertion
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71
