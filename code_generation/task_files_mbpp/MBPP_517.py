# MBPP/517
### Completion
def largest_pos(numbers):
    # Initialize the largest positive number to None
    largest = None
    
    # Iterate through the list of numbers
    for num in numbers:
        # Check if the number is positive and larger than the current largest
        if num > 0 and (largest is None or num > largest):
            largest = num
            
    return largest

# Test the function with the provided assertion
assert largest_pos([1, 2, 3, 4, -1]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_pos([1,2,3,4,-1]) == 4
    assert largest_pos([0,1,2,-5,-1,6]) == 6
    assert largest_pos([0,0,1,0]) == 1
