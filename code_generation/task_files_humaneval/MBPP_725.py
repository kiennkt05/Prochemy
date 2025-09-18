# MBPP/725
### Completion
import re

def extract_quotation(input_string):
    """
    Extracts values between double quotation marks from the given string.

    Args:
    input_string (str): The string from which to extract quoted values.

    Returns:
    list: A list of strings found between double quotation marks.
    """
    # Regex pattern to match text within double quotes
    pattern = r'"(.*?)"'
    
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

# Test case
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
    assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
