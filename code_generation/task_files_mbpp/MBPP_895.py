# MBPP/895
### Completion
def max_sum_subseq(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    # Create an array to store the maximum sum up to each index
    max_sum = [0] * n
    max_sum[0] = arr[0]
    max_sum[1] = max(arr[0], arr[1])
    
    for i in range(2, n):
        # Include the current element and add it to the max sum excluding the previous element
        include_current = arr[i] + max_sum[i - 2]
        # Exclude the current element
        exclude_current = max_sum[i - 1]
        # Take the maximum of including or excluding the current element
        max_sum[i] = max(include_current, exclude_current)
    
    return max_sum[-1]

# Test the function with the provided assertion
assert max_sum_subseq([1, 2, 9, 4, 5, 0, 4, 11, 6]) == 26
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_subseq([1, 2, 9, 4, 5, 0, 4, 11, 6]) == 26
    assert max_sum_subseq([1, 2, 9, 5, 6, 0, 5, 12, 7]) == 28
    assert max_sum_subseq([1, 3, 10, 5, 6, 0, 6, 14, 21]) == 44
