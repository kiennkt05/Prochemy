# MBPP/306
### Completion
def max_sum_increasing_subseq(arr, n, i, k):
    # Step 1: Extract the relevant part of the array
    prefix = arr[:i + 1]
    kth_element = arr[k]
    
    # Step 2: Initialize a list to store the maximum sum of increasing subsequences
    max_sum = [0] * (i + 1)
    
    # Step 3: Calculate the maximum sum of increasing subsequences up to index i
    for j in range(i + 1):
        max_sum[j] = prefix[j]  # Start with the value itself
        for m in range(j):
            if prefix[m] < prefix[j]:  # Check for increasing condition
                max_sum[j] = max(max_sum[j], max_sum[m] + prefix[j])
    
    # Step 4: Find the maximum sum including the kth element
    max_including_k = 0
    for j in range(i + 1):
        if prefix[j] < kth_element:  # Ensure the subsequence can include kth element
            max_including_k = max(max_including_k, max_sum[j] + kth_element)
    
    return max_including_k

# Test case
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
