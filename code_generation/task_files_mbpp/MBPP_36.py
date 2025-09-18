# MBPP/36
### Completion
def find_Nth_Digit(numerator, denominator, n):
    # Calculate the proper fraction
    fraction = numerator / denominator
    
    # Convert the fraction to a string
    fraction_str = str(fraction)
    
    # Find the position of the decimal point
    decimal_index = fraction_str.index('.')
    
    # Check if n is within the bounds of the digits after the decimal point
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    # Get the digits after the decimal point
    decimal_digits = fraction_str[decimal_index + 1:]
    
    # Check if the requested digit exists
    if n > len(decimal_digits):
        raise IndexError("The requested digit is out of bounds.")
    
    # Return the nth digit (1-based index)
    return int(decimal_digits[n - 1])

# Example usage
assert find_Nth_Digit(1, 2, 1) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Nth_Digit(1,2,1) == 5
    assert find_Nth_Digit(3,5,1) == 6
    assert find_Nth_Digit(5,6,5) == 3
