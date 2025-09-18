# MBPP/534
### Completion
def search_literal(literal, text):
    """
    Searches for the first occurrence of a literal string within another string
    and returns the starting and ending indices of the occurrence.

    Parameters:
    literal (str): The string to search for.
    text (str): The string in which to search.

    Returns:
    tuple: A tuple containing the starting and ending indices of the found literal,
           or None if the literal is not found.
    """
    start_index = text.find(literal)
    
    if start_index == -1:
        return None  # Literal not found
    
    end_index = start_index + len(literal)
    return (start_index, end_index)

# Test case
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
