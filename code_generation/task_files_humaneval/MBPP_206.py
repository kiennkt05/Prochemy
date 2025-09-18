# MBPP/206
### Completion
def concatenate_elements(input_tuple):
    """
    Concatenates adjacent elements in the given tuple.

    Args:
    input_tuple (tuple): A tuple of strings to concatenate.

    Returns:
    tuple: A tuple containing concatenated adjacent elements.
    """
    # Create a list to hold the concatenated results
    concatenated_list = []
    
    # Iterate through the tuple, stopping one element before the last
    for i in range(len(input_tuple) - 1):
        # Concatenate the current element with the next one
        concatenated_list.append(input_tuple[i] + input_tuple[i + 1])
    
    # Convert the list back to a tuple before returning
    return tuple(concatenated_list)

# Test the function with the provided test case
assert concatenate_elements(("DSP ", "IS ", "BEST ", "FOR ", "ALL ", "UTS")) == ('DSP IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL UTS')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_elements(("DSP ", "IS ", "BEST ", "FOR ", "ALL ", "UTS")) == ('DSP IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL UTS')
    assert concatenate_elements(("RES ", "IS ", "BEST ", "FOR ", "ALL ", "QESR")) == ('RES IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL QESR')
    assert concatenate_elements(("MSAM", "IS ", "BEST ", "FOR ", "ALL ", "SKD")) == ('MSAMIS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL SKD')
