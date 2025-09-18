# MBPP/254
### Completion
def words_ae(input_string):
    # Split the input string into words
    words = input_string.split()
    # Filter words that start with 'a' or 'e'
    result = [word for word in words if word.lower().startswith(('a', 'e'))]
    return result

# Test the function with the provided assertion
assert words_ae("python programe") == ['ame']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert words_ae("python programe")==['ame']
    assert words_ae("python programe language")==['ame','anguage']
    assert words_ae("assert statement")==['assert', 'atement']
