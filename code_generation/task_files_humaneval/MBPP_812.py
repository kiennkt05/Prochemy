# MBPP/812
### Completion
def road_rd(input_string):
    """
    Abbreviates 'Road' as 'Rd.' in the given input string.

    Parameters:
    input_string (str): The string in which to replace 'Road' with 'Rd.'

    Returns:
    str: The modified string with 'Road' replaced by 'Rd.'
    """
    # Replace 'Road' with 'Rd.'
    modified_string = input_string.replace("Road", "Rd.")
    return modified_string

# Test case
assert road_rd("ravipadu Road") == 'ravipadu Rd.'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert road_rd("ravipadu Road")==('ravipadu Rd.')
    assert road_rd("palnadu Road")==('palnadu Rd.')
    assert road_rd("eshwar enclave Road")==('eshwar enclave Rd.')
