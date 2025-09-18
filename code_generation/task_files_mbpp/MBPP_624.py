# MBPP/624
### Completion
def is_upper(s):
    return s.upper()

# Test the function
assert is_upper("person") == "PERSON"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_upper("person") =="PERSON"
    assert is_upper("final") == "FINAL"
    assert is_upper("Valid") == "VALID"
