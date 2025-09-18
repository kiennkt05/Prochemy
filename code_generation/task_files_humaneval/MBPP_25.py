# MBPP/25
### Completion
def find_Product(arr, n):
    """
    Function to find the product of non-repeated elements in a given array.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The length of the array (not used in the function but included as per the requirement).
    
    Returns:
    int: The product of non-repeated elements. If there are no non-repeated elements, return 1.
    """
    from collections import Counter
    
    # Count occurrences of each element
    element_count = Counter(arr)
    
    # Initialize product
    product = 1
    has_non_repeated = False
    
    # Iterate through the counted elements
    for element, count in element_count.items():
        if count == 1:  # Check for non-repeated elements
            product *= element
            has_non_repeated = True
    
    # If no non-repeated elements were found, return 1
    return product if has_non_repeated else 1

# Test case
assert find_Product([1, 1, 2, 3], 4) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Product([1,1,2,3],4) == 6
    assert find_Product([1,2,3,1,1],5) == 6
    assert find_Product([1,1,4,5,6],5) == 120
