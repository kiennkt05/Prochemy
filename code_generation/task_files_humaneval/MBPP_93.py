# MBPP/93
### Completion
def power(a, b):
    """
    Calculate the value of 'a' raised to the power of 'b'.
    
    Parameters:
    a (int or float): The base number.
    b (int): The exponent (should be a non-negative integer).
    
    Returns:
    int or float: The result of 'a' raised to the power of 'b'.
    """
    # Initialize result to 1 (as any number to the power of 0 is 1)
    result = 1
    
    # Multiply 'a' by itself 'b' times
    for _ in range(b):
        result *= a
    
    return result

# Test the function with the provided test case
assert power(3, 4) == 81

# Additional test cases (optional)
assert power(2, 3) == 8
assert power(5, 0) == 1
assert power(10, 2) == 100
assert power(7, 1) == 7

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125
