# MBPP/348
### Completion
def find_ways(n):
    # Dynamic programming table
    # dp[i] will store the number of valid sequences of length i
    dp = [0] * (n + 1)
    
    # Base case: There's one way to have a sequence of length 0 (the empty sequence)
    dp[0] = 1
    
    # Iterate over lengths from 1 to n
    for length in range(1, n + 1):
        # For each length, we can form valid sequences by adding a non-negative number
        # to all valid sequences of length-1
        dp[length] = dp[length - 1]  # Adding 0 to the previous sequences
        if length > 1:
            dp[length] += dp[length - 2]  # Adding 1 to the previous sequences
    
    return dp[n]

# Test the function with the provided assertion
assert find_ways(4) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_ways(4) == 2
    assert find_ways(6) == 5
    assert find_ways(8) == 14
