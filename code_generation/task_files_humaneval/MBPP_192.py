# MBPP/192
### Completion
def check_String(s):
    """
    Check if the input string contains at least one letter and one number.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string contains at least one letter and one number, False otherwise.
    """
    has_letter = False
    has_number = False
    
    for char in s:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        
        # If both conditions are met, we can return True early
        if has_letter and has_number:
            return True
    
    return False

# Test case
assert check_String('thishasboth29') == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_String('thishasboth29') == True
    assert check_String('python') == False
    assert check_String ('string') == False
