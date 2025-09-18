# MBPP/248
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
    
    # Calculate the harmonic sum for integers from 1 to n-1
    for k in range(1, n):
        total += 1 / k
    
    return total

# Test the function with the provided test case
assert harmonic_sum(7) == 2.5928571428571425

# You can add more test cases if needed
print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert harmonic_sum(7) == 2.5928571428571425
    assert harmonic_sum(4) == 2.083333333333333
    assert harmonic_sum(19) == 3.547739657143682
