# MBPP/971
### Completion
def maximum_segments(n, a, b, c):
    # Create a dp array initialized to -1
    dp = [-1] * (n + 1)
    dp[0] = 0  # Base case: 0 length can be formed with 0 segments

    # Iterate through each length from 1 to n
    for i in range(1, n + 1):
        # Check if we can form a segment of length a
        if i >= a and dp[i - a] != -1:
            dp[i] = max(dp[i], dp[i - a] + 1)
        # Check if we can form a segment of length b
        if i >= b and dp[i - b] != -1:
            dp[i] = max(dp[i], dp[i - b] + 1)
        # Check if we can form a segment of length c
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)

    return dp[n] if dp[n] != -1 else 0

# Test the function with the provided assertion
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
