# MBPP/563
### Completion
import re

def extract_values(s):
    # Use regular expression to find all occurrences of text within double quotes
    return re.findall(r'"(.*?)"', s)

# Test the function with the provided assertion
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert extract_values('"python","program","language"')==['python','program','language']
    assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']
