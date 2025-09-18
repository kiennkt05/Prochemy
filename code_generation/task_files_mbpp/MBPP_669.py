# MBPP/669
### Completion
import re

def check_IP(ip):
    # Regular expression for validating an IPv4 address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    
    if re.match(pattern, ip):
        return 'Valid IP address'
    else:
        return 'Invalid IP address'

# Test the function
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
