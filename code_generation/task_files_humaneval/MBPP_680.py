# MBPP/680
### Completion
def increasing_trend(sequence):
    """
    Check if the given sequence of numbers has an increasing trend.
    
    Parameters:
    sequence (list): A list of numbers to check for an increasing trend.
    
    Returns:
    bool: True if the sequence is strictly increasing, False otherwise.
    """
    # Iterate through the sequence and compare each element with the next
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False  # If any element is not less than the next, return False
    return True  # If all elements are in increasing order, return True

# Test case
assert increasing_trend([1, 2, 3, 4]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert increasing_trend([1,2,3,4]) == True
    assert increasing_trend([4,3,2,1]) == False
    assert increasing_trend([0,1,4,9]) == True
