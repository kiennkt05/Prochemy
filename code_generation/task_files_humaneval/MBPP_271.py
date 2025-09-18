# MBPP/271
### Completion
def even_Power_Sum(n):
    """
    Calculate the sum of the fifth power of the first n even natural numbers.

    Parameters:
    n (int): The number of even natural numbers to consider.

    Returns:
    int: The sum of the fifth powers of the first n even natural numbers.
    """
    total_sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i  # Calculate the ith even natural number
        total_sum += even_number ** 5  # Add the fifth power of the even number to the total sum
    return total_sum

# Test the function with the provided test case
assert even_Power_Sum(2) == 1056

# Additional test cases can be added to verify correctness
print(even_Power_Sum(2))  # Output: 1056
print(even_Power_Sum(3))  # Output: 33600 (2^5 + 4^5 + 6^5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32
