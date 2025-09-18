# MBPP/403
### Completion
import re

def is_valid_URL(url):
    # Regular expression for validating a URL
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # optional path

    return re.match(regex, url) is not None

# Test the function
assert is_valid_URL("https://www.google.com") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_valid_URL("https://www.google.com") == True
    assert is_valid_URL("https:/www.gmail.com") == False
    assert is_valid_URL("https:// www.redit.com") == False
