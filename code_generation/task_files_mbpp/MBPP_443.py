# MBPP/443
### Completion
def largest_neg(numbers):
    # Filter out the negative numbers from the list
    negative_numbers = [num for num in numbers if num < 0]
    
    # Return the largest negative number or None if there are no negative numbers
    return max(negative_numbers) if negative_numbers else None

# Test the function with the provided assertion
assert largest_neg([1, 2, 3, -4, -6]) == -6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1
