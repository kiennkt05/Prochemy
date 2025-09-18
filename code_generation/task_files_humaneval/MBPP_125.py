# MBPP/125
### Completion
def find_length(binary_string: str, length: int) -> int:
    # Initialize variables for Kadane's algorithm
    max_diff = float('-inf')  # This will hold the maximum difference found
    current_sum = 0  # This will hold the current sum of the transformed array

    # Iterate through each character in the binary string
    for char in binary_string:
        # Transform '0' to +1 and '1' to -1
        if char == '0':
            current_sum += 1
        else:  # char == '1'
            current_sum -= 1
        
        # Update the maximum difference found
        max_diff = max(max_diff, current_sum)
        
        # If current_sum drops below 0, reset it to 0
        if current_sum < 0:
            current_sum = 0

    return max_diff

# Test case
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
