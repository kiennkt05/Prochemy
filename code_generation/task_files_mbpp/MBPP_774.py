# MBPP/774
### Completion
import re

def check_email(email):
    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return 'Valid Email'
    else:
        return 'Invalid Email'

# Test the function with the provided assertion
assert check_email("ankitrai326@gmail.com") == 'Valid Email'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_email("ankitrai326@gmail.com") == 'Valid Email'
    assert check_email("my.ownsite@ourearth.org") == 'Valid Email'
    assert check_email("ankitaoie326.com") == 'Invalid Email'
