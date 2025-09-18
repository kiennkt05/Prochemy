# MBPP/967
### Completion
def check(s):
    # Define a set of vowels
    vowels = set('aeiou')
    # Convert the input string to lowercase and create a set of characters
    input_set = set(s.lower())
    # Check if all vowels are in the input set
    if vowels.issubset(input_set):
        return 'accepted'
    else:
        return 'not accepted'

# Test the function with the provided assertion
assert check("SEEquoiaL") == 'accepted'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check("SEEquoiaL") == 'accepted'
    assert check('program') == "not accepted"
    assert check('fine') == "not accepted"
