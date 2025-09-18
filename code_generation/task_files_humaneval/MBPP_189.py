# MBPP/189
### Completion
def first_Missing_Positive(nums):
    # Create a set of positive numbers from the input list
    positive_numbers = set(num for num in nums if num > 0)
    
    # Start checking from 1 upwards for the first missing positive integer
    i = 1
    while True:
        if i not in positive_numbers:
            return i
        i += 1

# Test case
assert first_Missing_Positive([1, 2, 3, -1, 5]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Missing_Positive([1,2,3,-1,5],5) == 4
    assert first_Missing_Positive([0,-1,-2,1,5,8],6) == 2
    assert first_Missing_Positive([0,1,2,5,-8],5) == 3
