# MBPP/593
### Completion
def removezero_ip(ip_address):
    """
    Remove leading zeroes from each octet of the given IP address.

    Parameters:
    ip_address (str): The IP address as a string.

    Returns:
    str: The IP address with leading zeroes removed from each octet.
    """
    # Split the IP address into its octets
    octets = ip_address.split('.')
    
    # Remove leading zeroes by converting each octet to an integer and back to string
    cleaned_octets = [str(int(octet)) for octet in octets]
    
    # Join the cleaned octets back into a single string
    return '.'.join(cleaned_octets)

# Test case
assert removezero_ip("216.08.094.196") == '216.8.94.196'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196') 
    assert removezero_ip("12.01.024")==('12.1.24') 
    assert removezero_ip("216.08.094.0196")==('216.8.94.196') 
