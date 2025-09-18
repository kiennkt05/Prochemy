# MBPP/918
### Completion
def coin_change(coins, num_coins, amount):
    # Create a list to store the number of ways to make change for each amount
    dp = [0] * (amount + 1)
    
    # There is one way to make change for 0 amount: use no coins
    dp[0] = 1
    
    # Iterate over each coin
    for coin in coins:
        # Update the dp array for all amounts from coin to the target amount
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    
    return dp[amount]

# Test the function with the provided assertion
assert coin_change([1, 2, 3], 3, 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert coin_change([1, 2, 3],3,4)==4
    assert coin_change([4,5,6,7,8,9],6,9)==2
    assert coin_change([4,5,6,7,8,9],6,4)==1
