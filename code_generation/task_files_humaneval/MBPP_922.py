# MBPP/922
### Completion
def max_product(arr):
    # Check if the array has at least two elements
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    
    # Sort the array
    arr.sort()
    
    # The two largest numbers
    max1 = arr[-1]
    max2 = arr[-2]
    
    # The two smallest numbers
    min1 = arr[0]
    min2 = arr[1]
    
    # Calculate the products
    product_max = max1 * max2
    product_min = min1 * min2
    
    # Determine which product is greater and return the corresponding pair
    if product_max >= product_min:
        return (max2, max1)  # Return in ascending order
    else:
        return (min1, min2)  # Return in ascending order

# Test case
assert max_product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_product([1, 2, 3, 4, 7, 0, 8, 4])==(7, 8)
    assert max_product([0, -1, -2, -4, 5, 0, -6])==(-4, -6)
    assert max_product([1, 3, 5, 6, 8, 9])==(8,9)
