# MBPP/531
### Completion
def min_coins(coins, num_coins, value):
    # Initialize a list to store the minimum coins for each value
    dp = [float('inf')] * (value + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the value 0

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for values from coin to value
        for v in range(coin, value + 1):
            dp[v] = min(dp[v], dp[v - coin] + 1)

    # If dp[value] is still infinity, it means it's not possible to form that value
    return dp[value] if dp[value] != float('inf') else -1

# Test the function with the provided assertion
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
