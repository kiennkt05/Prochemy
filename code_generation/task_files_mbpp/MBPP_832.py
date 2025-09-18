# MBPP/832
### Completion
import re

def extract_max(s):
    # Find all sequences of digits in the string
    numbers = re.findall(r'\d+', s)
    # Convert the found sequences to integers
    numbers = [int(num) for num in numbers]
    # Return the maximum value found, or None if no numbers were found
    return max(numbers) if numbers else None

# Test the function with the provided assertion
assert extract_max('100klh564abc365bg') == 564
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_max('100klh564abc365bg') == 564
    assert extract_max('hello300how546mer231') == 546
    assert extract_max('its233beenalong343journey234') == 343
