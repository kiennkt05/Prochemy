# MBPP/531
### Completion
def min_coins(coins, num_coins, target):
    # Initialize the dp array with a large number (infinity)
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the value 0

    # Fill the dp array
    for coin in coins:
        for value in range(coin, target + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    # If dp[target] is still infinity, it means we cannot form that value
    return dp[target] if dp[target] != float('inf') else -1

# Test case
assert min_coins([9, 6, 5, 1], 4, 11) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_coins([9, 6, 5, 1] ,4,11)==2
    assert min_coins([4,5,6,7,8,9],6,9)==1
    assert min_coins([1, 2, 3],3,4)==2
