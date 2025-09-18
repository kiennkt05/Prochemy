# MBPP/781
### Completion
def count_Divisors(n):
    """
    This function counts the number of divisors of a given integer n
    and returns "Even" if the count is even, and "Odd" if the count is odd.
    
    Parameters:
    n (int): The integer for which to count the divisors.
    
    Returns:
    str: "Even" if the count of divisors is even, "Odd" if it is odd.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    count = 0
    # Count the divisors
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    # Check if the count is even or odd
    if count % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test case
assert count_Divisors(10) == "Even"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Divisors(10) == "Even"
    assert count_Divisors(100) == "Odd"
    assert count_Divisors(125) == "Even"
