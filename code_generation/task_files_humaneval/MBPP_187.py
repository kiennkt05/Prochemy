# MBPP/187
### Completion
def longest_common_subsequence(X, Y, m, n):
    # Create a 2D array to store lengths of longest common subsequence
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the L array in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Characters match
                L[i][j] = L[i - 1][j - 1] + 1
            else:  # Characters do not match
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # The length of the longest common subsequence is in L[m][n]
    return L[m][n]

# Test case
assert longest_common_subsequence("AGGTAB", "GXTXAYB", 6, 7) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert longest_common_subsequence("AGGTAB" , "GXTXAYB", 6, 7) == 4
    assert longest_common_subsequence("ABCDGH" , "AEDFHR", 6, 6) == 3
    assert longest_common_subsequence("AXYT" , "AYZX", 4, 4) == 2
