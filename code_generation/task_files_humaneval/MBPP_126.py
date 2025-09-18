# MBPP/126
### Completion
def sum_of_common_divisors(a, b):
    """
    Calculate the sum of common divisors of two given numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of common divisors of a and b.
    """
    # Function to find all divisors of a number
    def find_divisors(n):
        divisors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.add(i)
        return divisors

    # Find divisors of both numbers
    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)

    # Find common divisors
    common_divisors = divisors_a.intersection(divisors_b)

    # Return the sum of common divisors
    return sum(common_divisors)

# Test the function with the provided test case
assert sum_of_common_divisors(10, 15) == 6  # Common divisors are 1 and 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3
