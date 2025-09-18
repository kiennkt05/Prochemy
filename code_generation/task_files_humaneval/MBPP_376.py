# MBPP/376
### Completion
def remove_replica(input_tuple, custom_value='MSP'):
    """
    Remove elements from the tuple that occur more than once and replace them with a custom value.

    Parameters:
    input_tuple (tuple): The input tuple from which duplicates will be removed.
    custom_value (str): The value to replace duplicates with. Default is 'MSP'.

    Returns:
    tuple: A new tuple with duplicates replaced by the custom value.
    """
    from collections import Counter

    # Count occurrences of each element in the tuple
    element_count = Counter(input_tuple)

    # Create a new tuple with duplicates replaced by custom_value
    result_tuple = tuple(custom_value if element_count[element] > 1 else element for element in input_tuple)

    return result_tuple

# Test case
assert remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
    assert remove_replica((2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9)) == (2, 3, 4, 'MSP', 5, 6, 'MSP', 7, 8, 9, 'MSP')
    assert remove_replica((2, 2, 5, 4, 5, 7, 5, 6, 7, 7)) == (2, 'MSP', 5, 4, 'MSP', 7, 'MSP', 6, 'MSP', 'MSP')
