# MBPP/727
### Completion
import re

def remove_char(input_string):
    # Use regex to replace all non-alphanumeric characters with an empty string
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)

# Test the function with the provided assertion
assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'
    assert remove_char("Hello1234:, ! Howare33u") == 'Hello1234Howare33u'
    assert remove_char("Cool543Triks@:, Make@987Trips") == 'Cool543TriksMake987Trips' 
