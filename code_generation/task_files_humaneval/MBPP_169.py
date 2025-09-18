# MBPP/169
### Completion
def get_pell(n):
    """
    Calculate the nth Pell number.

    Parameters:
    n (int): The index of the Pell number to calculate.

    Returns:
    int: The nth Pell number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two Pell numbers
    pell_0 = 0
    pell_1 = 1
    
    # Calculate Pell numbers iteratively
    for i in range(2, n + 1):
        pell_n = 2 * pell_1 + pell_0
        pell_0 = pell_1
        pell_1 = pell_n
    
    return pell_1

# Test the function with the provided test case
assert get_pell(4) == 12

# Additional test cases for verification
assert get_pell(0) == 0
assert get_pell(1) == 1
assert get_pell(2) == 2
assert get_pell(3) == 5
assert get_pell(5) == 29

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_pell(4) == 12
    assert get_pell(7) == 169
    assert get_pell(8) == 408
