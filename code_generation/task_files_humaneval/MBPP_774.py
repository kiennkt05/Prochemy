# MBPP/774
### Completion
import re

def check_email(email):
    """
    Check if the provided email address is valid.

    Parameters:
    email (str): The email address to check.

    Returns:
    str: 'Valid Email' if the email is valid, otherwise 'Invalid Email'.
    """
    # Define the regex pattern for a valid email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(email_pattern, email):
        return 'Valid Email'
    else:
        return 'Invalid Email'

# Test the function with the provided test case
assert check_email("ankitrai326@gmail.com") == 'Valid Email'

# Additional test cases
assert check_email("invalid-email") == 'Invalid Email'
assert check_email("user@domain.com") == 'Valid Email'
assert check_email("user.name@sub.domain.com") == 'Valid Email'
assert check_email("user@domain") == 'Invalid Email'
assert check_email("user@.com") == 'Invalid Email'
assert check_email("user@domain.c") == 'Invalid Email'
assert check_email("user@domain.co.uk") == 'Valid Email'

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_email("ankitrai326@gmail.com") == 'Valid Email'
    assert check_email("my.ownsite@ourearth.org") == 'Valid Email'
    assert check_email("ankitaoie326.com") == 'Invalid Email'
