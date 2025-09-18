# MBPP/512
### Completion
def count_element_freq(nested_tuple):
    """
    Count the frequency of elements in a mixed nested tuple.

    Args:
    nested_tuple (tuple): A tuple that may contain integers and nested tuples.

    Returns:
    dict: A dictionary with elements as keys and their frequencies as values.
    """
    frequency = {}

    def count_elements(t):
        for element in t:
            if isinstance(element, tuple):
                # If the element is a tuple, recurse into it
                count_elements(element)
            else:
                # If it's an integer, update its count in the frequency dictionary
                if element in frequency:
                    frequency[element] += 1
                else:
                    frequency[element] = 1

    # Start counting elements from the input tuple
    count_elements(nested_tuple)
    return frequency

# Test case
assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9)) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
    assert count_element_freq((6, 7, (6, 7), 8, (9, 10), 10) ) == {6: 2, 7: 2, 8: 1, 9: 1, 10: 2}
    assert count_element_freq((7, 8, (7, 8), 9, (10, 11), 11) ) == {7: 2, 8: 2, 9: 1, 10: 1, 11: 2}
