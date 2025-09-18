# MBPP/92
### Completion
def is_undulating(number: str) -> bool:
    """
    Check if the given number is undulating.
    
    An undulating number is defined as a number where no two adjacent digits are the same.
    
    Parameters:
    number (str): The string representation of the number to check.
    
    Returns:
    bool: True if the number is undulating, False otherwise.
    """
    # Check if the input is empty or has only one digit
    if len(number) < 2:
        return False
    
    # Iterate through the number and check adjacent digits
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            return False  # Found two adjacent digits that are the same
    
    return True  # All adjacent digits are different

# Test case
assert is_undulating("1212121") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_undulating("1212121") == True
    assert is_undulating("1991") == False
    assert is_undulating("121") == True
