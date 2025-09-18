# MBPP/109
### Completion
def odd_Equivalent(binary_string, length):
    # Initialize a counter for odd rotations
    odd_count = 0
    
    # Generate all rotations of the binary string
    for i in range(length):
        # Create the rotated string
        rotated_string = binary_string[i:] + binary_string[:i]
        
        # Check if the last character of the rotated string is '1'
        if rotated_string[-1] == '1':
            odd_count += 1
            
    return odd_count

# Test case
assert odd_Equivalent("011001", 6) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2
