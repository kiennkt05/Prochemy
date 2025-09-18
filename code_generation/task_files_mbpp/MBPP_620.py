# MBPP/620
### Completion
def largest_subset(arr, n):
    # Sort the array
    arr.sort()
    
    # Create a DP array to store the size of the largest divisible subset ending at each index
    dp = [1] * n
    
    # Variable to keep track of the maximum size of the subset
    max_size = 1
    
    # Build the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0:  # Check if arr[i] is divisible by arr[j]
                dp[i] = max(dp[i], dp[j] + 1)
        max_size = max(max_size, dp[i])
    
    return max_size

# Test the function with the provided assertion
assert largest_subset([1, 3, 6, 13, 17, 18], 6) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ], 6) == 4
    assert largest_subset([10, 5, 3, 15, 20], 5) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17], 6) == 4
