# MBPP/935
### Completion
def series_sum(n):
    """
    Calculate the sum of the series 1² + 2² + 3² + ... + n².

    Parameters:
    n (int): The upper limit of the series (must be a non-negative integer).

    Returns:
    int: The sum of the series.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2  # Square the current number and add to total_sum
    
    return total_sum

# Test case
assert series_sum(6) == 91  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert series_sum(6)==91
    assert series_sum(7)==140
    assert series_sum(12)==650
