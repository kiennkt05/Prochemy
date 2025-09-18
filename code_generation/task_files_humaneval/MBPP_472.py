# MBPP/472
### Completion
def check_Consecutive(numbers):
    # First, we check if the list is empty or has only one element
    if len(numbers) < 2:
        return True  # An empty list or a single element list is considered consecutive
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Check for consecutive numbers
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] != sorted_numbers[i - 1] + 1:
            return False  # Found a gap, not consecutive
    
    return True  # All numbers are consecutive

# Test case
assert check_Consecutive([1, 2, 3, 4, 5]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False
