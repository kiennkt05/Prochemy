# MBPP/178
### Completion
def string_literals(literals, text):
    for literal in literals:
        if literal in text:
            return 'Matched!'
    return 'Not Matched!'

# Example usage
assert string_literals(['language'], 'python language') == 'Matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_literals(['language'],'python language')==('Matched!')
    assert string_literals(['program'],'python language')==('Not Matched!')
    assert string_literals(['python'],'programming language')==('Not Matched!')
