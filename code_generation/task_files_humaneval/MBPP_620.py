# MBPP/620
### Completion
def largest_subset(arr, n):
    # Sort the array
    arr.sort()
    
    # Create a DP array to store the size of the largest divisible subset
    dp = [1] * n  # Each element is a subset of size 1 (itself)
    
    # Variable to keep track of the maximum size of the subset
    max_size = 1
    
    # Build the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0:  # Check if arr[j] divides arr[i]
                dp[i] = max(dp[i], dp[j] + 1)  # Update the size of the subset
        max_size = max(max_size, dp[i])  # Update the maximum size found
    
    return max_size

# Test case
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
