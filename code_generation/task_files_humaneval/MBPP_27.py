# MBPP/27
### Completion
def remove(strings):
    """
    Remove all digits from a list of strings.

    Parameters:
    strings (list of str): A list of strings from which digits will be removed.

    Returns:
    list of str: A new list containing the strings without any digits.
    """
    # Using list comprehension to iterate through each string and remove digits
    return [''.join(char for char in s if not char.isdigit()) for s in strings]

# Test case
assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
    assert remove(['28Jan','12Jan','11Jan']) == ['Jan','Jan','Jan']
    assert remove(['wonder1','wonder2','wonder3']) == ['wonder','wonder','wonder']
