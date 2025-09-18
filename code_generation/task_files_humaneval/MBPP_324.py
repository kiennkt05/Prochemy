# MBPP/324
### Completion
def sum_of_alternates(numbers):
    """
    Calculate the sum of integers at even and odd indices in the given tuple.

    Parameters:
    numbers (tuple): A tuple of integers.

    Returns:
    tuple: A tuple containing the sum of integers at even indices and the sum of integers at odd indices.
    """
    even_sum = 0
    odd_sum = 0
    
    for index, value in enumerate(numbers):
        if index % 2 == 0:  # Even index
            even_sum += value
        else:  # Odd index
            odd_sum += value
            
    return (even_sum, odd_sum)

# Test case
assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)
    assert sum_of_alternates((1, 2, 3, 4, 5)) == (6, 9)
    assert sum_of_alternates((6, 7, 8, 9, 4, 5)) == (21, 18)
