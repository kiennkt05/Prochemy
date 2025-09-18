# MBPP/748
### Completion
import re

def capital_words_spaces(s):
    # Use regex to find capital letters and add a space before them
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# Test the function with the provided assertion
assert capital_words_spaces("Python") == 'Python'

# Example usage
print(capital_words_spaces("HelloWorld"))  # Output: 'Hello World'
print(capital_words_spaces("ThisIsATest"))  # Output: 'This Is A Test'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'
