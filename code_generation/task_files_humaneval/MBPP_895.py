# MBPP/895
### Completion
def max_sum_subseq(arr):
    # Handle edge cases
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    # Initialize the dp array
    n = len(arr)
    dp = [0] * n
    
    # Base cases
    dp[0] = arr[0]
    if n > 1:
        dp[1] = max(arr[0], arr[1])
    
    # Fill the dp array using the recurrence relation
    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    # The last element of dp array contains the result
    return dp[-1]

# Test the function with the provided test case
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
