# MBPP/617
### Completion
def min_Jumps(jump_length, d):
    """
    Calculate the minimum number of jumps required to reach the point (d, 0) from the origin (0, 0).
    
    Parameters:
    jump_length (float): The length of each jump.
    d (float): The distance to the target point on the x-axis.
    
    Returns:
    float: The minimum number of jumps required to reach (d, 0).
    """
    # Calculate the number of full jumps
    full_jumps = d // jump_length
    
    # Calculate the remaining distance after full jumps
    remaining_distance = d % jump_length
    
    # If there is remaining distance, we need one more jump
    if remaining_distance > 0:
        return full_jumps + 1
    else:
        return full_jumps

# Test case
assert min_Jumps(3, 4) == 2  # 4 / 3 = 1 full jump + 1 remaining distance
assert min_Jumps(3, 11) == 4  # 11 / 3 = 3 full jumps + 2 remaining distance
assert min_Jumps(3, 9) == 3  # 9 / 3 = 3 full jumps, no remaining distance
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Jumps(3,4,11)==3.5
    assert min_Jumps(3,4,0)==0
    assert min_Jumps(11,14,11)==1
