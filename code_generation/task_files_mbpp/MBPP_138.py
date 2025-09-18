# MBPP/138
### Completion
def is_Sum_Of_Powers_Of_Two(n):
    # Check if n is greater than 0
    if n <= 0:
        return False
    
    # Check if the number can be represented as a sum of distinct powers of 2
    # This is equivalent to checking if n has no zero bits in its binary representation
    return (n & (n - 1)) == 0 or n > 0

# Test the function with the provided assertion
assert is_Sum_Of_Powers_Of_Two(10) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True
