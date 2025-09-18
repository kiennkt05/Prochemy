# MBPP/109
### Completion
def odd_Equivalent(binary_string, length):
    count = 0
    
    # Generate all rotations of the binary string
    for i in range(length):
        # Create the rotated string
        rotated_string = binary_string[i:] + binary_string[:i]
        
        # Convert the rotated binary string to decimal
        decimal_value = int(rotated_string, 2)
        
        # Check if the decimal value is odd
        if decimal_value % 2 == 1:
            count += 1
            
    return count

# Test the function with the provided assertion
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
