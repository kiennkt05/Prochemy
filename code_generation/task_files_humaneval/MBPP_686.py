# MBPP/686
### Completion
def freq_element(elements):
    """
    Function to find the frequency of each element in the given tuple.
    
    Args:
    elements (tuple): A tuple of elements to count frequencies.
    
    Returns:
    str: A string representation of the frequency dictionary.
    """
    frequency = {}
    
    # Count the frequency of each element
    for element in elements:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
            
    # Format the output as a string
    return str(frequency)

# Test case
assert freq_element((4, 5, 4, 5, 6, 6, 5, 5, 4)) == '{4: 3, 5: 4, 6: 2}'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert freq_element((4, 5, 4, 5, 6, 6, 5, 5, 4) ) == '{4: 3, 5: 4, 6: 2}'
    assert freq_element((7, 8, 8, 9, 4, 7, 6, 5, 4) ) == '{7: 2, 8: 2, 9: 1, 4: 2, 6: 1, 5: 1}'
    assert freq_element((1, 4, 3, 1, 4, 5, 2, 6, 2, 7) ) == '{1: 2, 4: 2, 3: 1, 5: 1, 2: 2, 6: 1, 7: 1}'
