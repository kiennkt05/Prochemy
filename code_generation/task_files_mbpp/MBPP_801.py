# MBPP/801
### Completion
def test_three_equal(a, b, c):
    # Initialize a counter for equal numbers
    count = 0
    
    # Check for equality and increment the counter
    if a == b:
        count += 1
    if b == c:
        count += 1
    if a == c:
        count += 1
    
    # If all three are equal, we should return 3
    if count == 3:
        return 3
    
    # Return the count of equal pairs
    return count

# Test the function with the provided assertion
assert test_three_equal(1, 1, 1) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert test_three_equal(1,1,1) == 3
    assert test_three_equal(-1,-2,-3) == 0
    assert test_three_equal(1,2,2) == 2
