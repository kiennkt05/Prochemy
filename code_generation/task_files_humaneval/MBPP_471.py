# MBPP/471
### Completion
def find_remainder(arr, n, mod):
    """
    Calculate the remainder of the product of an array divided by a given number.

    Parameters:
    arr (list): A list of integers to be multiplied.
    n (int): The number to divide the product by.
    mod (int): The modulus to apply to the product.

    Returns:
    int: The remainder of the product of the array elements divided by n.
    """
    product = 1
    for num in arr:
        product = (product * num) % n  # Take modulo n at each step to prevent overflow
    return product

# Test case
assert find_remainder([100, 10, 5, 25, 35, 14], 6, 11) == 9
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],6,11) ==9
    assert find_remainder([1,1,1],3,1) == 0
    assert find_remainder([1,2,1],3,2) == 0
