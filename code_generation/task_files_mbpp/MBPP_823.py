# MBPP/823
### Completion
import re

def check_substring(main_string, substring):
    # Create a regex pattern to check if the main_string starts with the substring
    pattern = f'^{re.escape(substring)}'
    
    # Use re.match to check if the main_string starts with the substring
    if re.match(pattern, main_string):
        return 'string starts with the given substring'
    else:
        return 'string doesnt start with the given substring'

# Test the function with the provided assertion
assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'
    assert check_substring("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'
    assert check_substring("Its been a long day", "been") == 'string doesnt start with the given substring'
