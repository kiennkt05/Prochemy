# MBPP/387
### Completion
def even_or_odd(hex_number):
    # Get the last character of the hexadecimal number
    last_char = hex_number[-1].upper()  # Convert to uppercase for consistency
    
    # Check if the last character represents an even number
    if last_char in '02468ACE':
        return "Even"
    else:
        return "Odd"

# Test the function with the provided assertion
assert even_or_odd("AB3454D") == "Odd"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_or_odd("AB3454D") =="Odd"
    assert even_or_odd("ABC") == "Even"
    assert even_or_odd("AAD") == "Odd"
