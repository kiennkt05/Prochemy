# MBPP/954
### Completion
def profit_amount(selling_price, cost_price):
    """
    Calculate the profit amount from selling price and cost price.
    
    Parameters:
    selling_price (float): The price at which the item is sold.
    cost_price (float): The price at which the item was purchased.
    
    Returns:
    float or None: The profit amount if there is a profit, otherwise None.
    """
    # Calculate profit
    profit = selling_price - cost_price
    
    # Return profit if it's greater than zero, otherwise return None
    return profit if profit > 0 else None

# Test case
assert profit_amount(1500, 1200) == 300
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert profit_amount(1500,1200)==300
    assert profit_amount(100,200)==None
    assert profit_amount(2000,5000)==None
