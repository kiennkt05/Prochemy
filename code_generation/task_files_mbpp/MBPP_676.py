# MBPP/676
### Completion
import re

def remove_extra_char(s):
    # Use regex to replace non-alphanumeric characters with an empty string
    return re.sub(r'[^a-zA-Z0-9]', '', s)

# Test the function with the provided assertion
assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'
    assert remove_extra_char('****//Google Flutter//*** - 36. ') == 'GoogleFlutter36'
    assert remove_extra_char('**//Google Firebase// - 478. ') == 'GoogleFirebase478'
