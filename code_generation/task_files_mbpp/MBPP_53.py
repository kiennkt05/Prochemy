# MBPP/53
### Completion
def check_Equality(s):
    if s and s[0] == s[-1]:  # Check if the string is not empty and first equals last
        return "Equal"
    else:
        return "Not Equal"

# Example assertion
assert check_Equality("abcda") == "Equal"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Equality("abcda") == "Equal"
    assert check_Equality("ab") == "Not Equal"
    assert check_Equality("mad") == "Not Equal"
