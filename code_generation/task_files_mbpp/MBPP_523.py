# MBPP/523
### Completion
def check_string(s):
    checks = [
        (lambda s: any(c.isupper() for c in s), 'String must have 1 upper case character.'),
        (lambda s: any(c.islower() for c in s), 'String must have 1 lower case character.'),
        (lambda s: any(c.isdigit() for c in s), 'String must have 1 number.'),
        (lambda s: len(s) >= 8, 'String length should be at least 8.')
    ]
    
    errors = [message for check, message in checks if not check(s)]
    return errors

# Example usage
assert check_string('python') == ['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be at least 8.']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_string('python')==['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.']
    assert check_string('123python')==['String must have 1 upper case character.']
    assert check_string('123Python')==['Valid string.']
