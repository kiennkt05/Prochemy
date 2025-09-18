# MBPP/246
### Completion
def babylonian_squareroot(x, tolerance=1e-10):
    """
    Compute the square root of a number using the Babylonian method.

    Parameters:
    x (float): The number to compute the square root of.
    tolerance (float): The acceptable error margin for the result.

    Returns:
    float: The square root of the number.
    """
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if x == 0:
        return 0.0
    
    # Initial guess
    guess = x / 2.0
    
    while True:
        # Calculate a new guess
        new_guess = (guess + x / guess) / 2.0
        
        # Check for convergence
        if abs(new_guess - guess) < tolerance:
            break
        
        guess = new_guess
    
    return new_guess

# Test case
assert abs(babylonian_squareroot(10) - 3.162277660168379) < 1e-10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert babylonian_squareroot(10)==3.162277660168379
    assert babylonian_squareroot(2)==1.414213562373095
    assert babylonian_squareroot(9)==3.0
