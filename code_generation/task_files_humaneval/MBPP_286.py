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
    max_sum_one = kadane(arr)

    # Step 2: Calculate the total sum of the array
    total_sum = sum(arr)

    # Step 3: Calculate the maximum prefix sum and maximum suffix sum
    max_prefix_sum = float('-inf')
    current_prefix_sum = 0
    for num in arr:
        current_prefix_sum += num
        max_prefix_sum = max(max_prefix_sum, current_prefix_sum)

    max_suffix_sum = float('-inf')
    current_suffix_sum = 0
    for num in reversed(arr):
        current_suffix_sum += num
        max_suffix_sum = max(max_suffix_sum, current_suffix_sum)

    # Step 4: Calculate the maximum sum for k > 1
    if k > 1:
        max_sum_k = max_prefix_sum + max_suffix_sum + (k - 2) * total_sum
    else:
        max_sum_k = float('-inf')

    # Step 5: Return the maximum of the two cases
    return max(max_sum_one, max_sum_k)

# Test case
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
