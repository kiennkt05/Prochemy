# MBPP/704
### Completion
def harmonic_sum(n):
    """
    Calculate the harmonic sum of n-1.
    
    Parameters:
    n (int): The upper limit for the harmonic sum calculation (exclusive).
    
    Returns:
    float: The harmonic sum of integers from 1 to n-1.
    """
    # Initialize the harmonic sum
    total = 0.0
    
    # Calculate the harmonic sum
    for k in range(1, n):
        total += 1 / k
    
    return total

# Test the function with the provided test case
assert harmonic_sum(10) == 2.9289682539682538

# You can add more test cases if needed
print("Harmonic sum of 10-1 is:", harmonic_sum(10))  # Expected output: 2.9289682539682538
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert harmonic_sum(10)==2.9289682539682538
    assert harmonic_sum(4)==2.083333333333333
    assert harmonic_sum(7)==2.5928571428571425 
