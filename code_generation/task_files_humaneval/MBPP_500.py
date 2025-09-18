# MBPP/500
### Completion
def concatenate_elements(elements):
    """
    Concatenates all elements of the given list into a single string with spaces in between.

    Args:
    elements (list): A list of strings to concatenate.

    Returns:
    str: A single string with all elements concatenated, separated by spaces.
    """
    # Join the elements with a space and return the result
    return ' '.join(elements)

# Test case
assert concatenate_elements(['hello', 'there', 'have', 'a', 'rocky', 'day']) == 'hello there have a rocky day'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_elements(['hello','there','have','a','rocky','day'] ) == '  hello there have a rocky day'
    assert concatenate_elements([ 'Hi', 'there', 'How','are', 'you'] ) == '  Hi there How are you'
    assert concatenate_elements([ 'Part', 'of', 'the','journey', 'is', 'end'] ) == '  Part of the journey is end'
