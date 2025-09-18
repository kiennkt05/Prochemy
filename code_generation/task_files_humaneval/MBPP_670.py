# MBPP/670
### Completion
def decreasing_trend(sequence):
    """
    Check if the given sequence of numbers has a decreasing trend.
    
    A sequence is considered to have a decreasing trend if each number
    is greater than the number that follows it.
    
    Parameters:
    sequence (list): A list of numbers to check.
    
    Returns:
    bool: True if the sequence has a decreasing trend, False otherwise.
    """
    # Iterate through the sequence and compare each element with the next
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            return False  # Found a pair that does not satisfy the decreasing condition
    return True  # All pairs satisfied the decreasing condition

# Test case
assert decreasing_trend([-4, -3, -2, -1]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decreasing_trend([-4,-3,-2,-1]) == True
    assert decreasing_trend([1,2,3]) == True
    assert decreasing_trend([3,2,1]) == False
