# MBPP/98
### Completion
def multiply_num(numbers):
    """
    Multiplies all the numbers in the input list and divides the result by the length of the list.
    
    Parameters:
    numbers (list or tuple): A list or tuple of numbers to be multiplied.
    
    Returns:
    float: The product of the numbers divided by the length of the list.
    """
    # Initialize the product to 1 (multiplicative identity)
    product = 1
    
    # Calculate the product of all numbers
    for num in numbers:
        product *= num
    
    # Get the length of the list
    length = len(numbers)
    
    # Divide the product by the length of the list
    result = product / length
    
    return result

# Test case
assert multiply_num((8, 2, 3, -1, 7)) == -67.2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_num((8, 2, 3, -1, 7))==-67.2
    assert multiply_num((-10,-20,-30))==-2000.0
    assert multiply_num((19,15,18))==1710.0
