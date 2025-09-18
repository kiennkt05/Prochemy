# MBPP/506
### Completion
from math import factorial

def permutation_coefficient(n, k):
    """
    Calculate the permutation coefficient P(n, k) which is the number of ways to arrange k items from n items.
    
    Parameters:
    n (int): The total number of items.
    k (int): The number of items to arrange.
    
    Returns:
    int: The permutation coefficient P(n, k).
    """
    if k > n:
        return 0  # If k is greater than n, the permutation is not defined.
    
    return factorial(n) // factorial(n - k)

# Test the function with the provided test case
assert permutation_coefficient(10, 2) == 90

# Additional test cases for verification
assert permutation_coefficient(5, 3) == 60  # 5! / (5-3)! = 5*4*3 = 60
assert permutation_coefficient(7, 0) == 1   # P(7, 0) = 1 (one way to arrange zero items)
assert permutation_coefficient(4, 5) == 0   # P(4, 5) = 0 (not possible)
assert permutation_coefficient(6, 2) == 30   # 6! / (6-2)! = 6*5 = 30

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert permutation_coefficient(10, 2) == 90
    assert permutation_coefficient(10, 3) == 720
    assert permutation_coefficient(10, 1) == 10
