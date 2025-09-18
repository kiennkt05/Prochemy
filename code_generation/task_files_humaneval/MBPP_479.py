# MBPP/479
### Completion
def first_Digit(number):
    """
    This function returns the first digit of a given number.
    
    Parameters:
    number (int): The number from which to extract the first digit.
    
    Returns:
    int: The first digit of the number.
    """
    # Convert the number to a string and get the first character
    first_digit_str = str(abs(number))[0]
    # Convert the first character back to an integer
    return int(first_digit_str)

# Test case
assert first_Digit(123) == 1

# Additional test cases for verification
assert first_Digit(-456) == 4  # Testing with a negative number
assert first_Digit(0) == 0      # Testing with zero
assert first_Digit(7890) == 7    # Testing with a larger number
assert first_Digit(-1001) == 1   # Testing with a negative number with leading zeros
assert first_Digit(5) == 5        # Testing with a single digit number

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1
