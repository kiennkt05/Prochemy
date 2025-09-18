# MBPP/832
### Completion
import re

def extract_max(s):
    """
    Extracts the maximum numeric value from a given string using regex.

    Parameters:
    s (str): The input string from which to extract numbers.

    Returns:
    int: The maximum numeric value found in the string. If no numbers are found, returns 0.
    """
    # Find all sequences of digits in the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the found sequences to integers
    int_numbers = [int(num) for num in numbers]
    
    # Return the maximum number found, or 0 if no numbers were found
    return max(int_numbers) if int_numbers else 0

# Test case
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
