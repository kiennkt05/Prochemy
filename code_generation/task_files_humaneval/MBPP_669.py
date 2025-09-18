# MBPP/669
### Completion
import re

def check_IP(ip_address):
    # Define the regex pattern for a valid IPv4 address
    pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
              r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
              r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
              r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    
    # Use regex to match the pattern
    if re.match(pattern, ip_address):
        return 'Valid IP address'
    else:
        return 'Invalid IP address'

# Test the function with the provided test case
assert check_IP("192.168.0.1") == 'Valid IP address'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_IP("192.168.0.1") == 'Valid IP address'
    assert check_IP("110.234.52.124") == 'Valid IP address'
    assert check_IP("366.1.2.2") == 'Invalid IP address'
