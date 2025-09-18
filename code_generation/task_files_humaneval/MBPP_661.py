# MBPP/661
### Completion
def max_sum_of_three_consecutive(arr, n):
    # Handle edge cases
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    
    # Initialize the dp array
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    
    # Fill the dp array
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])
    
    return dp[n-1]

# Test case
assert max_sum_of_three_consecutive([100, 1000, 100, 1000, 1], 5) == 2101
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_of_three_consecutive([100, 1000, 100, 1000, 1], 5) == 2101
    assert max_sum_of_three_consecutive([3000, 2000, 1000, 3, 10], 5) == 5013
    assert max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8], 8) == 27
