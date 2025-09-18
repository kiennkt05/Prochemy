# MBPP/452
### Completion
def loss_amount(original_amount, current_amount):
    if current_amount < original_amount:
        return original_amount - current_amount
    return None

# Example usage
assert loss_amount(1500, 1200) == 300
assert loss_amount(1500, 1500) == None
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert loss_amount(1500,1200)==None
    assert loss_amount(100,200)==100
    assert loss_amount(2000,5000)==3000
