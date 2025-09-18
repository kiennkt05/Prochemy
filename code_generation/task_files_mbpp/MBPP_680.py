# MBPP/680
### Completion
def increasing_trend(sequence):
    # Check if the sequence is empty or has only one element
    if len(sequence) < 2:
        return True
    
    # Iterate through the sequence and check if each number is less than the next
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
            
    return True

# Test the function with the provided assertion
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
