# MBPP/933
### Completion
import re

def camel_to_snake(camel_str):
    # Use regex to find the positions where a lowercase letter is followed by an uppercase letter
    # and replace it with the lowercase letter followed by an underscore and the lowercase version of the uppercase letter
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

# Test the function
assert camel_to_snake('GoogleAssistant') == 'google_assistant'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert camel_to_snake('GoogleAssistant') == 'google_assistant'
    assert camel_to_snake('ChromeCast') == 'chrome_cast'
    assert camel_to_snake('QuadCore') == 'quad_core'
