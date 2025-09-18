# MBPP/424
### Completion
def extract_rear(strings):
    """
    Extracts the last character of each string in the given tuple.

    Parameters:
    strings (tuple): A tuple containing strings.

    Returns:
    list: A list containing the last character of each string.
    """
    # Using list comprehension to extract the last character of each string
    return [s[-1] for s in strings]

# Test case
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']
