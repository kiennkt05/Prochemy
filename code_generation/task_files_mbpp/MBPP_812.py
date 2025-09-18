# MBPP/812
### Completion
def road_rd(input_string):
    return input_string.replace('Road', 'Rd.')

# Test the function
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
