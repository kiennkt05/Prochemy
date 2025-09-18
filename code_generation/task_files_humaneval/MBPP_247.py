# MBPP/247
### Completion
def lps(s: str) -> int:
    # Normalize the string by removing spaces and converting to uppercase
    s = s.replace(" ", "").upper()
    n = len(s)
    
    # Create a 2D array to store lengths of longest palindromic subsequences
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1  # end index of the substring
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # The result is in the top right corner of the table
    return dp[0][n - 1]

# Test case
assert lps("TENS FOR TENS") == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lps("TENS FOR TENS") == 5 
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9 
