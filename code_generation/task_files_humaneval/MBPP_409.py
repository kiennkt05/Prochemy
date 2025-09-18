# MBPP/409
### Completion
def min_product_tuple(tuples_list):
    """
    This function finds the minimum product from pairs of tuples within a given list.
    
    Parameters:
    tuples_list (list of tuples): A list containing tuples of two integers.
    
    Returns:
    int: The minimum product of the tuples.
    """
    # Initialize min_product to a large number
    min_product = float('inf')
    
    # Iterate through each tuple in the list
    for a, b in tuples_list:
        # Calculate the product of the current tuple
        product = a * b
        
        # Update min_product if the current product is smaller
        if product < min_product:
            min_product = product
            
    return min_product

# Test case
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
    assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
    assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100
