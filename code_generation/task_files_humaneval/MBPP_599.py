# MBPP/599
### Completion
def sum_average(n):
    """
    Calculate the sum and average of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider.

    Returns:
    tuple: A tuple containing the sum and average of the first n natural numbers.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    # Calculate the sum using the formula
    total_sum = n * (n + 1) // 2  # Using integer division for sum
    # Calculate the average
    average = total_sum / n
    
    return total_sum, average

# Test the function with the provided test case
assert sum_average(10) == (55, 5.5)

# Additional test cases
assert sum_average(1) == (1, 1.0)
assert sum_average(5) == (15, 3.0)
assert sum_average(100) == (5050, 50.5)

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)
