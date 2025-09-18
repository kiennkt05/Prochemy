# MBPP/459
### Completion
import re

def remove_uppercase(s: str) -> str:
    """
    Remove all uppercase letters from the given string using regex.

    Parameters:
    s (str): The input string from which uppercase letters will be removed.

    Returns:
    str: The modified string with all uppercase letters removed.
    """
    # Use regex to replace all uppercase letters with an empty string
    return re.sub(r'[A-Z]', '', s)

# Test case
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
