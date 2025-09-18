# MBPP/477
### Completion
def is_lower(input_string):
    return input_string.lower()

# Test the function
assert is_lower("InValid") == "invalid"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"
