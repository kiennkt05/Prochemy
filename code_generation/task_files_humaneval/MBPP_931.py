# MBPP/931
### Completion
def sum_series(n):
    """
    Calculate the sum of the series 1³ + 2³ + 3³ + ... + n³.

    Parameters:
    n (int): The upper limit of the series.

    Returns:
    int: The sum of the series.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 3
    return total_sum

# Test the function with the provided test case
assert sum_series(7) == 784

# Additional test cases
print(sum_series(1))  # Should return 1
print(sum_series(2))  # Should return 9 (1^3 + 2^3)
print(sum_series(3))  # Should return 36 (1^3 + 2^3 + 3^3)
print(sum_series(4))  # Should return 100 (1^3 + 2^3 + 3^3 + 4^3)
print(sum_series(5))  # Should return 225 (1^3 + 2^3 + 3^3 + 4^3 + 5^3)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_series(7)==784
    assert sum_series(5)==225
    assert sum_series(15)==14400
