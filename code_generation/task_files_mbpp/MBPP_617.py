# MBPP/617
### Completion
def min_Jumps(jump_length, d, y):
    # Since we are only interested in reaching (d, 0), y should always be 0
    if y != 0:
        raise ValueError("The y-coordinate must be 0.")
    
    # Calculate the number of jumps required to reach distance d
    jumps = d / jump_length
    
    return jumps

# Example usage
assert min_Jumps(3, 4, 0) == 4 / 3  # This should return approximately 1.33
assert min_Jumps(3, 11, 0) == 11 / 3  # This should return approximately 3.67
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Jumps(3,4,11)==3.5
    assert min_Jumps(3,4,0)==0
    assert min_Jumps(11,14,11)==1
