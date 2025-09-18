# MBPP/495
### Completion
import re

def remove_lowercase(s):
    # Use regex to replace all lowercase letters with an empty string
    return re.sub(r'[a-z]', '', s)

# Test the function with the provided assertion
assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'

# You can also add more test cases to verify the function
print(remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf'))  # Output: KDALOOOHLAJSI
print(remove_lowercase('HelloWorld'))  # Output: HWD
print(remove_lowercase('PythonIsFun'))  # Output: PIF
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
    assert remove_lowercase('ProducTnamEstreAmIngMediAplAYer') == 'PTEAIMAAY'
    assert remove_lowercase('maNufacTuredbYSheZenTechNolOGIes') == 'NTYSZTNOGI'
