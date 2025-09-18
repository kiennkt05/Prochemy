# MBPP/55
### Completion
def tn_gp(a, r, n):
    """
    Calculate the t-nth term of a geometric series.

    Parameters:
    a (int or float): The first term of the geometric series.
    r (int or float): The common ratio of the geometric series.
    n (int): The term number to find.

    Returns:
    int or float: The t-nth term of the geometric series.
    """
    # Calculate the n-th term using the formula a * r^(n-1)
    return a * (r ** (n - 1))

# Test case
assert tn_gp(1, 5, 2) == 16, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tn_gp(1,5,2)==16
    assert tn_gp(1,5,4)==256
    assert tn_gp(2,6,3)==486
