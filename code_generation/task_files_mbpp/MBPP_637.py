# MBPP/637
### Completion
def noprofit_noloss(selling_price, cost_price):
    return selling_price == cost_price

# Test the function with the provided assertion
assert noprofit_noloss(1500, 1200) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert noprofit_noloss(1500,1200)==False
    assert noprofit_noloss(100,100)==True
    assert noprofit_noloss(2000,5000)==False
