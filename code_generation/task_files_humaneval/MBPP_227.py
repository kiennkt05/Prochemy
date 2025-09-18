# MBPP/227
### Completion
def min_of_three(a, b, c):
    """
    Returns the minimum of three numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The minimum of the three numbers.
    """
    return min(a, b, c)

# Test case
assert min_of_three(10, 20, 0) == 0

# Additional test cases for verification
assert min_of_three(-1, -5, -3) == -5
assert min_of_three(5, 5, 5) == 5
assert min_of_three(1.5, 2.5, 0.5) == 0.5

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_of_three(10,20,0)==0
    assert min_of_three(19,15,18)==15
    assert min_of_three(-10,-20,-30)==-30
