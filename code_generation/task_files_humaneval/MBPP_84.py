# MBPP/84
### Completion
def sequence(n):
    """
    Calculate the n-th number in the Newman-Conway sequence.

    Parameters:
    n (int): The position in the Newman-Conway sequence to retrieve.

    Returns:
    int: The n-th number in the Newman-Conway sequence.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    if n == 1 or n == 2:
        return 1
    
    # Initialize the sequence list with base cases
    P = [0] * (n + 1)  # We use n+1 to make indexing easier
    P[1] = 1
    P[2] = 1
    
    # Fill the sequence using the recursive definition
    for i in range(3, n + 1):
        P[i] = P[P[i - 1]] + P[i - P[i - 1]]
    
    return P[n]

# Test case
assert sequence(10) == 6

# Additional test cases for verification
assert sequence(1) == 1
assert sequence(2) == 1
assert sequence(3) == 2
assert sequence(4) == 3
assert sequence(5) == 3
assert sequence(6) == 4
assert sequence(7) == 5
assert sequence(8) == 5
assert sequence(9) == 6

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2
