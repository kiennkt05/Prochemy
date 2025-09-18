# MBPP/598
### Completion
def armstrong_number(num):
    """
    Check if the given number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if num is an Armstrong number, False otherwise.
    """
    # Convert the number to string to iterate over digits
    digits = str(num)
    # Calculate the number of digits
    num_digits = len(digits)
    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Test case
assert armstrong_number(153) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False
