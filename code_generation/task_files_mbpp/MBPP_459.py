# MBPP/459
### Completion
import re

def remove_uppercase(s):
    # Use regex to replace uppercase substrings with an empty string
    return re.sub(r'[A-Z]+', '', s)

# Test the function with the provided assertion
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
