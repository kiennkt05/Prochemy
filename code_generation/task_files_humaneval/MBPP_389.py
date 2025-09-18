# MBPP/389
### Completion
def find_lucas(n):
    """
    Calculate the n-th Lucas number.

    Parameters:
    n (int): The index of the Lucas number to find.

    Returns:
    int: The n-th Lucas number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    # Initialize the first two Lucas numbers
    lucas_0 = 2
    lucas_1 = 1
    
    # Compute the n-th Lucas number iteratively
    for i in range(2, n + 1):
        lucas_n = lucas_0 + lucas_1
        lucas_0 = lucas_1
        lucas_1 = lucas_n
    
    return lucas_n

# Test the function with the provided assertion
assert find_lucas(9) == 76

# You can add more test cases if needed
print("The 9th Lucas number is:", find_lucas(9))  # Output: 76
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4
