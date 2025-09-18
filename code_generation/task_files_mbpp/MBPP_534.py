# MBPP/534
### Completion
def search_literal(pattern, text):
    start_index = text.find(pattern)
    if start_index == -1:
        return None  # Return None if the pattern is not found
    end_index = start_index + len(pattern)
    return (start_index, end_index)

# Test the function with the provided assertion
assert search_literal('python', 'python programming language') == (0, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert search_literal('python','python programming language')==(0,6)
    assert search_literal('programming','python programming language')==(7,18)
    assert search_literal('language','python programming language')==(19,27)
