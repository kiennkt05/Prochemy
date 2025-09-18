# MBPP/495
### Completion
import re

def remove_lowercase(s: str) -> str:
    """
    Remove all lowercase substrings from the given string using regex.

    Parameters:
    s (str): The input string from which lowercase letters will be removed.

    Returns:
    str: The modified string with all lowercase letters removed.
    """
    # Use regex to substitute all lowercase letters with an empty string
    result = re.sub(r'[a-z]', '', s)
    return result

# Test case
assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
    assert remove_lowercase('ProducTnamEstreAmIngMediAplAYer') == 'PTEAIMAAY'
    assert remove_lowercase('maNufacTuredbYSheZenTechNolOGIes') == 'NTYSZTNOGI'
