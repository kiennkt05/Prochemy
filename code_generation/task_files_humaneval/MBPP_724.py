# MBPP/724
### Completion
def power_base_sum(base, power):
    """
    Calculate the sum of all digits of the base raised to the specified power.

    Parameters:
    base (int): The base number.
    power (int): The exponent to which the base is raised.

    Returns:
    int: The sum of the digits of the result.
    """
    # Step 1: Calculate base raised to the power
    result = base ** power
    
    # Step 2: Convert the result to string to access each digit
    result_str = str(result)
    
    # Step 3: Sum the digits
    digit_sum = sum(int(digit) for digit in result_str)
    
    # Step 4: Return the sum of the digits
    return digit_sum

# Test case
assert power_base_sum(2, 100) == 115
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert power_base_sum(2,100)==115
    assert power_base_sum(8,10)==37
    assert power_base_sum(8,15)==62
