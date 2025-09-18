# MBPP/647
### Completion
import re

def split_upperstring(s):
    """
    Splits the input string at each uppercase letter.

    Parameters:
    s (str): The input string to be split.

    Returns:
    list: A list of substrings split at uppercase letters.
    """
    # Use regex to find all uppercase letters and split the string
    # The regex pattern '(?=[A-Z])' is a lookahead assertion that matches positions before uppercase letters
    return re.findall(r'[A-Z][^A-Z]*', s)

# Test case
assert split_upperstring("PythonProgramLanguage") == ['Python', 'Program', 'Language']

# Additional test cases for verification
assert split_upperstring("HelloWorld") == ['Hello', 'World']
assert split_upperstring("ThisIsATest") == ['This', 'Is', 'ATest']
assert split_upperstring("SplitAtUppercase") == ['Split', 'At', 'Uppercase']
assert split_upperstring("A") == ['A']
assert split_upperstring("") == []  # Edge case: empty string

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_upperstring("PythonProgramLanguage")==['Python','Program','Language']
    assert split_upperstring("PythonProgram")==['Python','Program']
    assert split_upperstring("ProgrammingLanguage")==['Programming','Language']
