# MBPP/575
### Completion
def count_no(n, m, start, end):
    """
    Find the nth number in a sequence from start to end that is not a multiple of m.

    Parameters:
    n (int): The position in the sequence to find (1-based index).
    m (int): The number to avoid multiples of.
    start (int): The starting point of the sequence (inclusive).
    end (int): The ending point of the sequence (inclusive).

    Returns:
    int: The nth number in the sequence that is not a multiple of m.
    """
    # List to hold numbers that are not multiples of m
    non_multiples = []
    
    # Iterate through the range from start to end
    for number in range(start, end + 1):
        if number % m != 0:  # Check if the number is not a multiple of m
            non_multiples.append(number)
    
    # Check if we have enough non-multiples to return the nth one
    if n <= len(non_multiples):
        return non_multiples[n - 1]  # Return the nth number (1-based index)
    else:
        raise ValueError("There are not enough non-multiples in the given range.")

# Test case
assert count_no(2, 3, 1, 10) == 5  # The second number not a multiple of 3 in range 1 to 10 is 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_no(2,3,1,10) == 5
    assert count_no(3,6,4,20) == 11
    assert count_no(5,10,4,20) == 16
