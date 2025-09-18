# MBPP/563
### Completion
import re

def extract_values(s):
    """
    Extracts values between double quotation marks from the input string.

    Parameters:
    s (str): The input string containing quoted values.

    Returns:
    list: A list of strings extracted from within the quotation marks.
    """
    # Use regular expression to find all occurrences of text within double quotes
    matches = re.findall(r'"(.*?)"', s)
    return matches

# Test the function with the provided test case
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']

# Additional test cases
assert extract_values('"Hello, World!", "Test"') == ['Hello, World!', 'Test']
assert extract_values('No quotes here') == []
assert extract_values('"Single" "Double" "Triple"') == ['Single', 'Double', 'Triple']

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert extract_values('"python","program","language"')==['python','program','language']
    assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']
