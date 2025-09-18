# MBPP/637
### Completion
def noprofit_noloss(selling_price, cost_price):
    """
    Check if there is no profit and no loss.
    
    Parameters:
    selling_price (float): The price at which the item is sold.
    cost_price (float): The price at which the item was bought.
    
    Returns:
    bool: True if there is no profit and no loss, False otherwise.
    """
    return selling_price == cost_price

# Test case
assert noprofit_noloss(1500, 1200) == False  # Selling price is not equal to cost price
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert noprofit_noloss(1500,1200)==False
    assert noprofit_noloss(100,100)==True
    assert noprofit_noloss(2000,5000)==False
