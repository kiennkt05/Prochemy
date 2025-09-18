# MBPP/971
### Completion
def maximum_segments(n, a, b, c):
    # Initialize the dp array with a very small number
    dp = [-float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 length can be formed with 0 segments

    # Iterate through each length from 1 to n
    for i in range(1, n + 1):
        # Check if we can form the length i using segments of length a, b, or c
        if i >= a:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i >= b:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i >= c:
            dp[i] = max(dp[i], dp[i - c] + 1)

    # If dp[n] is still negative infinity, it means we cannot form length n
    return dp[n] if dp[n] >= 0 else 0

# Test case
assert maximum_segments(7, 5, 2, 5) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum_segments(7, 5, 2, 5) == 2
    assert maximum_segments(17, 2, 1, 3) == 17
    assert maximum_segments(18, 16, 3, 6) == 6
