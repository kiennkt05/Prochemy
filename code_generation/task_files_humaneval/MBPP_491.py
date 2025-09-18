# MBPP/491
### Completion
def sum_gp(a, n, r):
    """
    Calculate the sum of the first n terms of a geometric progression.

    Parameters:
    a (int or float): The first term of the GP.
    n (int): The number of terms to sum.
    r (int or float): The common ratio of the GP.

    Returns:
    float: The sum of the first n terms of the GP.
    """
    if r == 1:
        # If the common ratio is 1, the series is constant
        return a * n
    else:
        # Using the formula for the sum of a geometric series
        return a * (1 - r**n) / (1 - r)

# Test the function with the provided test case
assert sum_gp(1, 5, 2) == 31, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_gp(1,5,2)==31
    assert sum_gp(1,5,4)==341
    assert sum_gp(2,6,3)==728
