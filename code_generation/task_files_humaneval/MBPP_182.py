# MBPP/182
### Completion
import re

def find_character(s):
    # Find all uppercase letters
    uppercase = re.findall(r'[A-Z]', s)
    # Find all lowercase letters
    lowercase = re.findall(r'[a-z]', s)
    # Find all special characters
    special_characters = re.findall(r'[^A-Za-z0-9]', s)
    # Find all numeric values
    numeric_values = re.findall(r'[0-9]', s)
    
    return (uppercase, lowercase, special_characters, numeric_values)

# Test case
assert find_character("ThisIsGeeksforGeeks") == (['T', 'I', 'G', 'G'], ['h', 'i', 's', 's', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'e', 'e', 'k', 's'], [], [])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_character("ThisIsGeeksforGeeks") == (['T', 'I', 'G', 'G'], ['h', 'i', 's', 's', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'e', 'e', 'k', 's'], [], [])
    assert find_character("Hithere2") == (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], [])
    assert find_character("HeyFolks32") == (['H', 'F'], ['e', 'y', 'o', 'l', 'k', 's'], ['3', '2'], [])
