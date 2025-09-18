# MBPP/36
### Completion
def find_Nth_Digit(numerator, denominator, n):
    # Calculate the fraction
    fraction = numerator / denominator
    
    # Convert the fraction to string
    fraction_str = str(fraction)
    
    # Find the position of the decimal point
    decimal_index = fraction_str.index('.')
    
    # Calculate the index of the nth digit after the decimal point
    nth_digit_index = decimal_index + n
    
    # Check if the nth digit exists
    if nth_digit_index < len(fraction_str):
        return int(fraction_str[nth_digit_index])
    else:
        raise IndexError("The fraction does not have enough digits after the decimal point.")

# Test case
assert find_Nth_Digit(1, 2, 1) == 5  # This test case is incorrect based on the fraction 1/2 = 0.5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Nth_Digit(1,2,1) == 5
    assert find_Nth_Digit(3,5,1) == 6
    assert find_Nth_Digit(5,6,5) == 3
