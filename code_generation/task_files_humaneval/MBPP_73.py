# MBPP/73
### Completion
import re

def multiple_split(input_string):
    """
    Splits the input string using multiple delimiters: newline and asterisk.
    
    Args:
    input_string (str): The string to be split.
    
    Returns:
    list: A list of substrings obtained by splitting the input string.
    """
    # Define the regex pattern for delimiters: newline (\n) and asterisk (*)
    pattern = r'[\n*]'
    
    # Use re.split to split the string based on the defined pattern
    result = re.split(pattern, input_string)
    
    return result

# Test case
assert multiple_split('Forces of the \ndarkness*are coming into the play.') == ['Forces of the ', 'darkness', 'are coming into the play.']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiple_split('Forces of the \ndarkness*are coming into the play.') == ['Forces of the ', 'darkness', 'are coming into the play.']
    assert multiple_split('Mi Box runs on the \n Latest android*which has google assistance and chromecast.') == ['Mi Box runs on the ', ' Latest android', 'which has google assistance and chromecast.']
    assert multiple_split('Certain services\nare subjected to change*over the seperate subscriptions.') == ['Certain services', 'are subjected to change', 'over the seperate subscriptions.']
