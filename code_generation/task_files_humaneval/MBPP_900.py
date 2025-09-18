# MBPP/900
### Completion
def match_num(s: str) -> bool:
    """
    Check if the input string starts with the number '5'.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string starts with '5', False otherwise.
    """
    # Check if the string starts with '5'
    return s.startswith('5')

# Test case
assert match_num('5-2345861') == True  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert match_num('5-2345861')==True
    assert match_num('6-2345861')==False
    assert match_num('78910')==False
