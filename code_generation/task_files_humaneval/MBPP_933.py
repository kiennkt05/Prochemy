# MBPP/933
### Completion
import re

def camel_to_snake(camel_case_str):
    """
    Convert a camel case string to a snake case string.

    Parameters:
    camel_case_str (str): The camel case string to convert.

    Returns:
    str: The converted snake case string.
    """
    # Use regex to find uppercase letters and replace them with _lowercase
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
    return snake_case_str

# Test case
assert camel_to_snake('GoogleAssistant') == 'google_assistant'

# Additional test cases
assert camel_to_snake('ThisIsATest') == 'this_is_a_test'
assert camel_to_snake('AnotherExampleHere') == 'another_example_here'
assert camel_to_snake('Simple') == 'simple'
assert camel_to_snake('OneMoreTestCase') == 'one_more_test_case'

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert camel_to_snake('GoogleAssistant') == 'google_assistant'
    assert camel_to_snake('ChromeCast') == 'chrome_cast'
    assert camel_to_snake('QuadCore') == 'quad_core'
