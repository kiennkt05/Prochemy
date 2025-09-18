# MBPP/120
### Completion
def max_product_tuple(tuples_list):
    """
    Function to find the maximum product from pairs of tuples within a given list.
    
    Parameters:
    tuples_list (list of tuples): A list containing tuples of two integers.
    
    Returns:
    int: The maximum product of the pairs in the list.
    """
    # Initialize max_product to a very small number
    max_product = float('-inf')
    
    # Iterate through each tuple in the list
    for a, b in tuples_list:
        # Calculate the product of the current tuple
        product = a * b
        
        # Update max_product if the current product is greater
        if product > max_product:
            max_product = product
            
    return max_product

# Test case
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484
