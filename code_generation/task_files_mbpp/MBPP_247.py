# MBPP/247
### Completion
def lps(s: str) -> int:
    # Preprocess the string to ignore spaces and consider case insensitivity
    s = s.replace(" ", "").lower()
    n = len(s)
    
    # Create a 2D array to store lengths of longest palindromic subsequences
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the dp array
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1  # end index of the substring
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]  # characters match
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # characters do not match
    
    return dp[0][n - 1]  # The result is in the top right corner of the matrix

# Test the function with the provided assertion
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
