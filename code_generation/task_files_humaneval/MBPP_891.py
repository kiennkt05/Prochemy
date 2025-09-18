# MBPP/891
### Completion
def same_length(num1, num2):
    """
    Check if two numbers have the same number of digits.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    bool: True if both numbers have the same number of digits, False otherwise.
    """
    # Convert numbers to strings and count the length
    len_num1 = len(str(abs(num1)))  # Use abs to handle negative numbers
    len_num2 = len(str(abs(num2)))  # Use abs to handle negative numbers
    
    # Compare the lengths
    return len_num1 == len_num2

# Test case
assert same_length(12, 1) == False  # 12 has 2 digits, 1 has 1 digit
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert same_Length(12,1) == False
    assert same_Length(2,2) == True
    assert same_Length(10,20) == True
