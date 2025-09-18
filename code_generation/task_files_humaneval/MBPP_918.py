# MBPP/918
### Completion
def coin_change(coins, num_coins, amount):
    # Create a list to store the number of ways to make change for each amount
    dp = [0] * (amount + 1)
    
    # Base case: There is one way to make change for amount 0
    dp[0] = 1
    
    # Iterate over each coin
    for coin in coins:
        # Update the dp list for all amounts from coin to the target amount
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    # The answer is the number of ways to make change for the target amount
    return dp[amount]

# Test case
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
