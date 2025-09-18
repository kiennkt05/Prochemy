# MBPP/543
### Completion
def count_digits(num1, num2):
    """
    Adds two numbers and returns the number of digits in the sum.

    Parameters:
    num1 (int): The first number to add.
    num2 (int): The second number to add.

    Returns:
    int: The number of digits in the sum of num1 and num2.
    """
    # Calculate the sum of the two numbers
    total = num1 + num2
    
    # Convert the sum to a string and count the number of digits
    num_digits = len(str(total))
    
    return num_digits

# Test the function with the provided assertion
assert count_digits(9875, 10) == 4

# You can add more test cases if needed
print("Test passed successfully.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_digits(9875,10)==(4)
    assert count_digits(98759853034,100)==(11)
    assert count_digits(1234567,500)==(7)
