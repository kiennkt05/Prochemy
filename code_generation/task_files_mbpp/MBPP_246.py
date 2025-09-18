# MBPP/246
### Completion
def babylonian_squareroot(n, tolerance=1e-10):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0:
        return 0
    
    # Initial guess will be n / 2
    guess = n / 2.0
    
    while True:
        # Calculate a new guess
        new_guess = (guess + n / guess) / 2
        
        # Check for convergence
        if abs(new_guess - guess) < tolerance:
            return new_guess
        
        guess = new_guess

# Test the function with the provided assertion
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
