# MBPP/325
### Completion
def get_Min_Squares(n):
    # Create a list to store the minimum number of squares for each number up to n
    dp = [float('inf')] * (n + 1)
    
    # Base case: 0 can be represented by 0 squares
    dp[0] = 0
    
    # Iterate through all numbers from 1 to n
    for i in range(1, n + 1):
        # Check all squares less than or equal to i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
            
    return dp[n]

# Test the function with the provided assertion
assert get_Min_Squares(6) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Min_Squares(6) == 3
    assert get_Min_Squares(2) == 2
    assert get_Min_Squares(4) == 1
