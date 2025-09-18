# MBPP/150
### Completion
def does_Contain_B(B, D, N):
    """
    Check if the number N is present in the infinite sequence starting from B with a step size of D.
    
    Parameters:
    B (int): The starting number of the sequence.
    D (int): The step size of the sequence.
    N (int): The number to check for presence in the sequence.
    
    Returns:
    bool: True if N is in the sequence, False otherwise.
    """
    # If D is 0, the sequence does not progress, so we can only check if B equals N
    if D == 0:
        return B == N
    
    # Calculate the difference from B
    difference = N - B
    
    # Check if the difference is non-negative and divisible by D
    return difference >= 0 and difference % D == 0

# Test case
assert does_Contain_B(1, 7, 3) == True  # This should return True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert does_Contain_B(1,7,3) == True
    assert does_Contain_B(1,-3,5) == False
    assert does_Contain_B(3,2,5) == False
