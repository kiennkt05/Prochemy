# MBPP/286
### Completion
def max_sub_array_sum_repeated(arr, k):
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Step 1: Calculate the maximum subarray sum for the original array
    max_kadane = kadane(arr)
    
    # Step 2: Calculate the total sum of the original array
    total_sum = sum(arr)
    
    # Step 3: Handle different cases based on the value of k
    if k == 1:
        return max_kadane
    elif k == 2:
        # We can consider the maximum subarray sum in the original array and the first repetition
        return max(max_kadane, max_kadane + kadane(arr + arr))
    else:
        # For k > 2, we can consider the maximum subarray that spans across the boundaries
        max_prefix_sum = float('-inf')
        current_prefix_sum = 0
        for i in range(len(arr)):
            current_prefix_sum += arr[i]
            max_prefix_sum = max(max_prefix_sum, current_prefix_sum)
        
        max_suffix_sum = float('-inf')
        current_suffix_sum = 0
        for i in range(len(arr) - 1, -1, -1):
            current_suffix_sum += arr[i]
            max_suffix_sum = max(max_suffix_sum, current_suffix_sum)
        
        # The maximum sum can be the best of:
        # 1. The maximum subarray sum in the original array
        # 2. The maximum subarray sum in two repetitions
        # 3. The sum of the best prefix + (k-2) * total_sum + best suffix
        return max(max_kadane, 
                   max_prefix_sum + max_suffix_sum + (k - 2) * total_sum)

# Example usage
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
