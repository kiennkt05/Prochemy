# MBPP/647
### Completion
import re

def split_upperstring(s):
    # Use regular expression to split the string at uppercase letters
    return re.findall(r'[A-Z][a-z]*', s)

# Test the function with the provided assertion
assert split_upperstring("PythonProgramLanguage") == ['Python', 'Program', 'Language']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_upperstring("PythonProgramLanguage")==['Python','Program','Language']
    assert split_upperstring("PythonProgram")==['Python','Program']
    assert split_upperstring("ProgrammingLanguage")==['Programming','Language']
