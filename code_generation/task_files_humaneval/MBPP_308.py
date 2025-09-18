# MBPP/308
### Completion
def large_product(list1, list2, n):
    """
    Find the specified number of largest products from two given lists.

    Parameters:
    list1 (list): The first list of numbers.
    list2 (list): The second list of numbers.
    n (int): The number of largest products to return.

    Returns:
    list: A list of the n largest products.
    """
    # Generate all possible products from the two lists
    products = [a * b for a in list1 for b in list2]
    
    # Sort the products in descending order
    products.sort(reverse=True)
    
    # Return the top n products
    return products[:n]

# Test case
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]
