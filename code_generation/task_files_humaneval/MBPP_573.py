# MBPP/573
### Completion
def unique_product(numbers):
    """
    Calculate the product of unique numbers in the given list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The product of unique integers in the list.
    """
    # Use a set to get unique numbers
    unique_numbers = set(numbers)
    
    # Initialize product to 1 (multiplicative identity)
    product = 1
    
    # Calculate the product of unique numbers
    for number in unique_numbers:
        product *= number
    
    return product

# Test case
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert unique_product([1, 2, 3, 1,]) == 6
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0
