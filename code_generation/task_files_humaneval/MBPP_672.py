# MBPP/672
### Completion
def max_of_three(a, b, c):
    """
    Returns the maximum of three numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The maximum of the three numbers.
    """
    return max(a, b, c)

# Test case
assert max_of_three(10, 20, 30) == 30

# Additional test cases for verification
assert max_of_three(5, 5, 5) == 5
assert max_of_three(-1, -2, -3) == -1
assert max_of_three(100, 50, 75) == 100
assert max_of_three(0, 0, 0) == 0

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_of_three(10,20,30)==30
    assert max_of_three(55,47,39)==55
    assert max_of_three(10,49,30)==49
