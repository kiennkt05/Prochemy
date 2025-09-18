# MBPP/330
### Completion
import re

def find_char(input_string):
    # Regex pattern to match words of length 3, 4, or 5
    pattern = r'\b\w{3,5}\b'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

# Test case
assert find_char('For the four consumer complaints contact manager AKR reddy') == ['For', 'the', 'four', 'AKR', 'reddy']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_char('For the four consumer complaints contact manager AKR reddy') == ['For', 'the', 'four', 'AKR', 'reddy']
    assert find_char('Certain service are subject to change MSR') == ['are', 'MSR']
    assert find_char('Third party legal desclaimers') == ['Third', 'party', 'legal']
