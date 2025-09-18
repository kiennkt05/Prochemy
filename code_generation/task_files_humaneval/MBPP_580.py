# MBPP/580
### Completion
def extract_even(nested_tuple):
    """
    Extracts even elements from a nested mixed tuple.
    
    Args:
    nested_tuple (tuple): A tuple that may contain integers and other tuples.
    
    Returns:
    tuple: A new tuple containing only the even integers and processed nested tuples.
    """
    result = []
    
    for element in nested_tuple:
        if isinstance(element, int):  # Check if the element is an integer
            if element % 2 == 0:  # Check if the integer is even
                result.append(element)
        elif isinstance(element, tuple):  # Check if the element is a tuple
            # Recursively extract even elements from the nested tuple
            even_nested = extract_even(element)
            if even_nested:  # Only add if the result is not empty
                result.append(even_nested)
    
    return tuple(result)  # Convert the result list back to a tuple

# Test case
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)
