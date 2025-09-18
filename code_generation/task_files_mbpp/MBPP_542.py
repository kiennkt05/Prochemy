# MBPP/542
### Completion
import re

def fill_spaces(input_string):
    # Use regex to replace spaces, commas, or dots with a colon
    return re.sub(r'[ ,.]', ':', input_string)

# Test the function with the provided assertion
assert fill_spaces('Boult Curve Wireless Neckband') == 'Boult:Curve:Wireless:Neckband'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert fill_spaces('Boult Curve Wireless Neckband') == 'Boult:Curve:Wireless:Neckband'
    assert fill_spaces('Stereo Sound Sweatproof') == 'Stereo:Sound:Sweatproof'
    assert fill_spaces('Probass Curve Audio') == 'Probass:Curve:Audio'
