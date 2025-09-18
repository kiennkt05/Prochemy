# MBPP/270
### Completion
def sum_even_and_even_index(numbers, _):
    """
    Calculate the sum of even numbers located at even indices in the list.

    Parameters:
    numbers (list): A list of integers.
    _ (int): An additional parameter that is not used in the calculation.

    Returns:
    int: The sum of even numbers at even indices.
    """
    total_sum = 0
    
    # Iterate through the list with index
    for index in range(len(numbers)):
        # Check if the index is even and the number is even
        if index % 2 == 0 and numbers[index] % 2 == 0:
            total_sum += numbers[index]
    
    return total_sum

# Test case
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8], 6) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8],6) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18],10) == 26
    assert sum_even_and_even_index([5, 6, 12, 1],4) == 12
