# MBPP/747
### Completion
def lcs_of_three(str1, str2, str3, len1, len2, len3):
    # Create a 3D array to store lengths of longest common subsequence
    dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for __ in range(len1 + 1)]

    # Build the dp array
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[len1][len2][len3]

# Test the function with the provided assertion
assert lcs_of_three('AGGT12', '12TXAYB', '12XBA', 6, 7, 5) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA', 6, 7, 5) == 2
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels', 5, 8, 13) == 5 
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea', 7, 6, 5) == 3
