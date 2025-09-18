# MBPP/923
### Completion
def lcs_length(str1, str2):
    # Create a 2D array to store lengths of longest common subsequence
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array from the bottom up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def super_seq(str1, str2, len1, len2):
    # Calculate the length of the longest common subsequence
    lcs_len = lcs_length(str1, str2)
    
    # Calculate the length of the shortest common supersequence
    scs_length = len1 + len2 - lcs_len
    return scs_length

# Test case
assert super_seq("AGGTAB", "GXTXAYB", 6, 7) == 9
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert super_seq("AGGTAB", "GXTXAYB", 6, 7) == 9
    assert super_seq("feek", "eke", 4, 3) == 5
    assert super_seq("PARRT", "RTA", 5, 3) == 6
