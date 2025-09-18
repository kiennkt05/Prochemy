# MBPP/207
### Completion
def find_longest_repeating_subseq(s):
    n = len(s)
    # Create a 2D array to store lengths of longest repeating subsequences
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If characters match and indices are not the same
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]

# Test the function with the provided assertion
assert find_longest_repeating_subseq("AABEBCDD") == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_longest_repeating_subseq("AABEBCDD") == 3
    assert find_longest_repeating_subseq("aabb") == 2
    assert find_longest_repeating_subseq("aab") == 1
