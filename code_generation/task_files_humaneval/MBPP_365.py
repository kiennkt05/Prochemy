# MBPP/365
### Completion
def count_Digit(number):
    """
    Count the number of digits in a given number.

    Parameters:
    number (int): The number whose digits are to be counted.

    Returns:
    int: The count of digits in the number.
    """
    # Convert the number to its absolute value and then to a string
    # to count the digits. We use str() to handle the number as a string.
    return len(str(abs(number)))

# Test case
assert count_Digit(12345) == 5  # This should pass without any assertion error

# Additional test cases for verification
assert count_Digit(-12345) == 5  # Negative number should also return 5
assert count_Digit(0) == 1        # Zero has 1 digit
assert count_Digit(100) == 3      # 100 has 3 digits
assert count_Digit(999999) == 6   # 999999 has 6 digits

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Digit(12345) == 5
    assert count_Digit(11223305) == 8
    assert count_Digit(4123459) == 7
