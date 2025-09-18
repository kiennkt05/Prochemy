# MBPP/748
### Completion
import re

def capital_words_spaces(s: str) -> str:
    """
    Insert spaces before capital letters in the given string.
    
    Args:
    s (str): The input string to process.
    
    Returns:
    str: The modified string with spaces inserted before capital letters.
    """
    # Use regex to find positions where a capital letter follows a lowercase letter or another capital letter
    # The pattern looks for a position where a capital letter is preceded by a lowercase letter or another capital letter
    modified_string = re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', s)
    
    return modified_string

# Test case
assert capital_words_spaces("Python") == 'Python'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'
