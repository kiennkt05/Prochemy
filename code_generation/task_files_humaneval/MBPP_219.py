# MBPP/219
### Completion
def extract_min_max(input_tuple, k):
    """
    Extracts the minimum and maximum k elements from the given tuple.

    Parameters:
    input_tuple (tuple): A tuple of numbers.
    k (int): The number of minimum and maximum elements to extract.

    Returns:
    tuple: A tuple containing the minimum k elements followed by the maximum k elements.
    """
    # Convert the tuple to a sorted list
    sorted_list = sorted(input_tuple)
    
    # Extract the minimum k elements
    min_elements = sorted_list[:k]
    
    # Extract the maximum k elements
    max_elements = sorted_list[-k:]
    
    # Combine the results and return as a tuple
    return (*min_elements, *max_elements)

# Test case
assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
    assert extract_min_max((4, 5, 6, 1, 2, 7), 3) == (1, 2, 4, 5, 6, 7)
    assert extract_min_max((2, 3, 4, 8, 9, 11, 7), 4) == (2, 3, 4, 7, 8, 9, 11)
