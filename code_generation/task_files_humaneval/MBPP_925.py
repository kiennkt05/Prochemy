# MBPP/925
### Completion
def multiple_tuple(numbers):
    """
    Calculate the product of all the numbers in the given tuple.

    Parameters:
    numbers (tuple): A tuple containing numeric values.

    Returns:
    int or float: The product of all the numbers in the tuple.
    """
    product = 1  # Initialize product to 1
    for number in numbers:
        product *= number  # Multiply each number to the product
    return product

# Test the function with the provided test case
assert multiple_tuple((4, 3, 2, 2, -1, 18)) == -864

# You can add more test cases if needed
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert mutiple_tuple((4, 3, 2, 2, -1, 18)) == -864
    assert mutiple_tuple((1,2,3)) == 6
    assert mutiple_tuple((-2,-4,-6)) == -48
