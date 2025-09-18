# MBPP/822
### Completion
import re

def pass_validity(password):
    # Check the length of the password
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return False
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

# Test the function with the provided assertion
assert pass_validity("password") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pass_validity("password")==False
    assert pass_validity("Password@10")==True
    assert pass_validity("password@10")==False
