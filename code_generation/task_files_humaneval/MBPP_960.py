# MBPP/960
### Completion
def get_noOfways(n):
    # Base cases
    if n == 0:
        return 1  # 1 way to tile a 2x0 board (do nothing)
    elif n == 1:
        return 1  # 1 way to tile a 2x1 board (one vertical domino)
    elif n == 2:
        return 2  # 2 ways to tile a 2x2 board (two vertical or two horizontal)

    # Initialize an array to store the number of ways to tile boards of length 0 to n
    dp = [0] * (n + 1)
    dp[0] = 1  # 1 way to tile a 2x0 board
    dp[1] = 1  # 1 way to tile a 2x1 board
    dp[2] = 2  # 2 ways to tile a 2x2 board

    # Fill the dp array using the recursive relation
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Test the function with the provided test case
assert get_noOfways(4) == 3  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_noOfways(4)==3
    assert get_noOfways(3)==2
    assert get_noOfways(5)==5
