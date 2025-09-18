# MBPP/500
### Completion
def concatenate_elements(elements):
    return ' ' + ' '.join(elements)

# Test the function with the provided assertion
assert concatenate_elements(['hello', 'there', 'have', 'a', 'rocky', 'day']) == ' hello there have a rocky day'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_elements(['hello','there','have','a','rocky','day'] ) == '  hello there have a rocky day'
    assert concatenate_elements([ 'Hi', 'there', 'How','are', 'you'] ) == '  Hi there How are you'
    assert concatenate_elements([ 'Part', 'of', 'the','journey', 'is', 'end'] ) == '  Part of the journey is end'
