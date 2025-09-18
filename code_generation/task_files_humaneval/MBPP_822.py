# MBPP/822
### Completion
import re

def pass_validity(password: str) -> bool:
    """
    Check if the provided password is valid based on the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character

    Args:
    password (str): The password to validate.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

# Test the function with the provided assertion
assert pass_validity("password") == False  # This should return False as "password" does not meet the criteria.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pass_validity("password")==False
    assert pass_validity("Password@10")==True
    assert pass_validity("password@10")==False
