# MBPP/804
### Completion
def is_Product_Even(numbers, n):
    """
    Check if the product of the numbers in the list is even.

    Parameters:
    numbers (list): A list of integers.
    n (int): The number of elements in the list.

    Returns:
    bool: True if the product is even, False otherwise.
    """
    # Check if any number in the list is even
    for number in numbers:
        if number % 2 == 0:  # If the number is even
            return True
    return False  # If no even number was found

# Test case
assert is_Product_Even([1, 2, 3], 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Product_Even([1,2,3],3) == True
    assert is_Product_Even([1,2,1,4],4) == True
    assert is_Product_Even([1,1],2) == False
