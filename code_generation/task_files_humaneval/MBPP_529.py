# MBPP/529
### Completion
def jacobsthal_lucas(n):
    """
    Calculate the nth Jacobsthal-Lucas number.

    The Jacobsthal-Lucas numbers are defined as:
    J(0) = 2
    J(1) = 1
    J(n) = J(n-1) + 2 * J(n-2) for n >= 2

    Parameters:
    n (int): The index of the Jacobsthal-Lucas number to compute.

    Returns:
    int: The nth Jacobsthal-Lucas number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    # Initialize the first two Jacobsthal-Lucas numbers
    j0, j1 = 2, 1
    
    # Compute the nth Jacobsthal-Lucas number iteratively
    for i in range(2, n + 1):
        j_next = j1 + 2 * j0
        j0, j1 = j1, j_next
    
    return j1

# Test the function with the provided assertion
assert jacobsthal_lucas(5) == 31

# Additional test cases (optional)
print(jacobsthal_lucas(0))  # Output: 2
print(jacobsthal_lucas(1))  # Output: 1
print(jacobsthal_lucas(2))  # Output: 4
print(jacobsthal_lucas(3))  # Output: 7
print(jacobsthal_lucas(4))  # Output: 14
print(jacobsthal_lucas(5))  # Output: 31
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert jacobsthal_lucas(5) == 31
    assert jacobsthal_lucas(2) == 5
    assert jacobsthal_lucas(4) == 17
