# MBPP/348
### Completion
def find_ways(n):
    # Base case: if n is 0, there's one way to have an empty sequence
    if n == 0:
        return 1
    
    # Initialize a list to store the number of ways to form sequences of each length
    dp = [0] * (n + 1)
    dp[0] = 1  # There's one way to have a sequence of length 0 (the empty sequence)
    
    # Iterate through lengths from 1 to n
    for length in range(1, n + 1):
        # For each length, we can add a value of 1 or -1
        # We need to ensure that the prefix sum remains non-negative
        for value in [1, -1]:
            if length - 1 >= 0 and (value == 1 or dp[length - 1] > 0):
                dp[length] += dp[length - 1]
    
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
