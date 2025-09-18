# MBPP/403
### Completion
import re

def is_valid_URL(url):
    # Define the regex pattern for a valid URL
    pattern = re.compile(
        r'^(https?://)'  # Protocol (http or https)
        r'((www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6})'  # Domain name
        r'(:\d+)?'  # Optional port
        r'(/.*)?$'  # Optional path, query, and fragment
    )
    
    # Use the fullmatch method to check if the entire URL matches the pattern
    return bool(pattern.fullmatch(url))

# Test the function with the provided test case
assert is_valid_URL("https://www.google.com") == True

# Additional test cases for validation
assert is_valid_URL("http://example.com") == True
assert is_valid_URL("https://example.com/path/to/resource") == True
assert is_valid_URL("http://example.com:8080") == True
assert is_valid_URL("https://example.com/path?query=1#fragment") == True
assert is_valid_URL("ftp://example.com") == False  # Invalid protocol
assert is_valid_URL("http://-example.com") == False  # Invalid domain
assert is_valid_URL("http://example..com") == False  # Invalid domain
assert is_valid_URL("http://example.com:abc") == False  # Invalid port

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_valid_URL("https://www.google.com") == True
    assert is_valid_URL("https:/www.gmail.com") == False
    assert is_valid_URL("https:// www.redit.com") == False
