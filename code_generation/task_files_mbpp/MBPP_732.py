# MBPP/732
### Completion
def replace_specialchar(text):
    # Replace spaces, commas, and dots with a colon
    return text.replace(' ', ':').replace(',', ':').replace('.', ':')

# Test the function with the provided assertion
assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
    assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
    assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')
