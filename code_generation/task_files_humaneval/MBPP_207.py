# MBPP/207
### Completion
def find_longest_repeating_subseq(s: str) -> int:
    n = len(s)
    # Create a 2D array to store lengths of longest repeating subsequences
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if characters match and are not at the same position
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the longest repeating subsequence will be in dp[n][n]
    return dp[n][n]

# Test case
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
