# MBPP/189
### Completion
def first_Missing_Positive(nums, n):
    # Create a set of the positive numbers in the list
    positive_numbers = set(num for num in nums if num > 0)
    
    # Check for the first missing positive number
    for i in range(1, n + 1):
        if i not in positive_numbers:
            return i
            
    # If all numbers from 1 to n are present, return n + 1
    return n + 1

# Test the function with the provided assertion
assert first_Missing_Positive([1, 2, 3, -1, 5], 5) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Missing_Positive([1,2,3,-1,5],5) == 4
    assert first_Missing_Positive([0,-1,-2,1,5,8],6) == 2
    assert first_Missing_Positive([0,1,2,5,-8],5) == 3
