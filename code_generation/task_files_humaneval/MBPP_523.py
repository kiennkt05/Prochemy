# MBPP/523
### Completion
def check_string(s):
    # Define the checks using lambda functions
    has_upper = lambda x: any(c.isupper() for c in x)
    has_lower = lambda x: any(c.islower() for c in x)
    has_digit = lambda x: any(c.isdigit() for c in x)
    is_valid_length = lambda x: len(x) >= 8
    
    # Initialize an empty list to collect error messages
    errors = []
    
    # Check each condition and append error messages if conditions are not met
    if not has_upper(s):
        errors.append('String must have 1 upper case character.')
    if not has_lower(s):
        errors.append('String must have 1 lower case character.')
    if not has_digit(s):
        errors.append('String must have 1 number.')
    if not is_valid_length(s):
        errors.append('String length should be at least 8.')
    
    return errors

# Test case
assert check_string('python') == ['String must have 1 upper case character.', 
                                   'String must have 1 number.', 
                                   'String length should be at least 8.']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_string('python')==['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.']
    assert check_string('123python')==['String must have 1 upper case character.']
    assert check_string('123Python')==['Valid string.']
