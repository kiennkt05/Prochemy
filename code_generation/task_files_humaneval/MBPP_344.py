# MBPP/344
### Completion
import math

def count_Odd_Squares(start, end):
    # Calculate the smallest integer whose square is >= start
    lower_bound = math.ceil(math.sqrt(start))
    # Calculate the largest integer whose square is <= end
    upper_bound = math.floor(math.sqrt(end))
    
    # The count of perfect squares is the number of integers from lower_bound to upper_bound
    if lower_bound > upper_bound:
        return 0  # No perfect squares in the range
    
    return upper_bound - lower_bound + 1

# Test case
assert count_Odd_Squares(5, 100) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Odd_Squares(5,100) == 8
    assert count_Odd_Squares(8,65) == 6
    assert count_Odd_Squares(2,5) == 1
