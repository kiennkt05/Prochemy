# MBPP/954
### Completion
def profit_amount(selling_price, cost_price):
    profit = selling_price - cost_price
    return profit if profit > 0 else None

# Test the function with the provided assertion
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
