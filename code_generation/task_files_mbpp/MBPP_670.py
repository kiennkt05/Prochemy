# MBPP/670
### Completion
def decreasing_trend(sequence):
    # Check if the sequence is empty or has only one element
    if len(sequence) < 2:
        return False
    
    # Iterate through the sequence and check for decreasing trend
    for i in range(1, len(sequence)):
        if sequence[i] >= sequence[i - 1]:
            return False
            
    return True

# Test the function with the provided assertion
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
