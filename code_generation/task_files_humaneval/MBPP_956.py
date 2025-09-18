# MBPP/956
### Completion
import re

def split_list(s):
    """
    Splits the input string at uppercase letters.

    Args:
    s (str): The input string to be split.

    Returns:
    list: A list of substrings split at uppercase letters.
    """
    # Use regex to find all sequences that start with an uppercase letter
    return re.findall(r'[A-Z][a-z]*', s)

# Test case
assert split_list("LearnToBuildAnythingWithGoogle") == ['Learn', 'To', 'Build', 'Anything', 'With', 'Google']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_list("LearnToBuildAnythingWithGoogle") == ['Learn', 'To', 'Build', 'Anything', 'With', 'Google']
    assert split_list("ApmlifyingTheBlack+DeveloperCommunity") == ['Apmlifying', 'The', 'Black+', 'Developer', 'Community']
    assert split_list("UpdateInTheGoEcoSystem") == ['Update', 'In', 'The', 'Go', 'Eco', 'System']
