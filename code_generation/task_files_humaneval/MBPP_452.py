# MBPP/452
### Completion
def loss_amount(initial_amount, final_amount):
    """
    Calculate the loss amount if the final amount is less than the initial amount.
    
    Parameters:
    initial_amount (float): The initial amount before any loss.
    final_amount (float): The final amount after potential loss.
    
    Returns:
    float or None: The loss amount if there is a loss, otherwise None.
    """
    # Check if there is a loss
    if final_amount < initial_amount:
        # Calculate the loss amount
        return initial_amount - final_amount
    else:
        # No loss
        return None

# Test cases
assert loss_amount(1500, 1200) == 300  # There is a loss of 300
assert loss_amount(1500, 1500) == None  # No loss
assert loss_amount(1500, 1600) == None  # No loss
assert loss_amount(1000, 800) == 200    # There is a loss of 200
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert loss_amount(1500,1200)==None
    assert loss_amount(100,200)==100
    assert loss_amount(2000,5000)==3000
