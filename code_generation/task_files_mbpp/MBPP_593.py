# MBPP/593
### Completion
def removezero_ip(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')
    # Remove leading zeroes from each octet and convert to int to avoid leading zeroes
    cleaned_octets = [str(int(octet)) for octet in octets]
    # Join the cleaned octets back into an IP address
    return '.'.join(cleaned_octets)

# Test the function with the provided assertion
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
