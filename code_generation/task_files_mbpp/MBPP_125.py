# MBPP/125
### Completion
def find_length(binary_string, length):
    # Transform the binary string into a list of +1 and -1
    transformed = [1 if char == '0' else -1 for char in binary_string]
    
    # Initialize variables for Kadane's algorithm
    max_ending_here = max_so_far = transformed[0]
    
    # Apply Kadane's algorithm
    for x in transformed[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Test the function with the provided assertion
assert find_length("11000010001", 11) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_length("11000010001", 11) == 6
    assert find_length("10111", 5) == 1
    assert find_length("11011101100101", 14) == 2 
