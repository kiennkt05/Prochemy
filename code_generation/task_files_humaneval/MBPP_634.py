# MBPP/634
### Completion
def even_Power_Sum(n):
    """
    Calculate the sum of the fourth power of the first n even natural numbers.

    Parameters:
    n (int): The number of even natural numbers to consider.

    Returns:
    int: The sum of the fourth powers of the first n even natural numbers.
    """
    total_sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i  # Calculate the ith even natural number
        total_sum += even_number ** 4  # Add the fourth power of the even number to the total sum
    return total_sum

# Test the function with the provided test case
assert even_Power_Sum(2) == 272

# Additional test cases
print(even_Power_Sum(1))  # Should return 16 (2^4)
print(even_Power_Sum(3))  # Should return 272 + 1296 = 1568 (2^4 + 4^4 + 6^4)
print(even_Power_Sum(4))  # Should return 272 + 1296 + 4096 = 5376 (2^4 + 4^4 + 6^4 + 8^4)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_Power_Sum(2) == 272
    assert even_Power_Sum(3) == 1568
    assert even_Power_Sum(4) == 5664
