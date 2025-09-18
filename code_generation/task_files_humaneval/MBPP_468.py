# MBPP/468
### Completion
def max_product(arr, n):
    # Edge case: if the array is empty or has only one element
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    # Initialize dp array where dp[i] will hold the maximum product of increasing subsequence ending at index i
    dp = [0] * n
    
    # Each element is a subsequence of itself
    for i in range(n):
        dp[i] = arr[i]
    
    # Build the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:  # Check for increasing condition
                dp[i] = max(dp[i], dp[j] * arr[i])  # Update dp[i] with the maximum product
    
    # The result is the maximum value in dp array
    return max(dp)

# Test case
assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000 
    assert max_product([4, 42, 55, 68, 80], 5) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000 
