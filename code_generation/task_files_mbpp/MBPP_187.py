# MBPP/187
### Completion
def longest_common_subsequence(X, Y, m, n):
    # Create a 2D array to store lengths of longest common subsequence
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the L array in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS for X[0..m-1], Y[0..n-1]
    return L[m][n]

# Test the function with the provided assertion
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
