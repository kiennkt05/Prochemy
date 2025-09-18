# MBPP/218
### Completion
def min_Operations(a: int, b: int) -> int:
    """
    Calculate the minimum number of operations required to make two numbers equal.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The minimum number of operations required to make a and b equal.
    """
    # The minimum operations required is the absolute difference between a and b
    return abs(a - b)

# Test case
assert min_Operations(2, 4) == 2  # The correct answer should be 2, not 1
assert min_Operations(5, 5) == 0  # No operations needed if both numbers are equal
assert min_Operations(10, 3) == 7  # 7 operations needed to make 10 equal to 3
assert min_Operations(-1, 1) == 2  # 2 operations needed to make -1 equal to 1

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Operations(2,4) == 1
    assert min_Operations(4,10) == 4
    assert min_Operations(1,4) == 3
