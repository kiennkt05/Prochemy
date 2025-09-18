# MBPP/220
### Completion
import re

def replace_max_specialchar(input_string, n):
    """
    Replace up to n occurrences of spaces, commas, or dots in the input string with a colon.

    Parameters:
    input_string (str): The string in which to replace characters.
    n (int): The maximum number of occurrences to replace.

    Returns:
    str: The modified string with up to n replacements.
    """
    # Define a replacement function that keeps track of the number of replacements made
    def replacement(match):
        nonlocal count
        if count < n:
            count += 1
            return ':'
        return match.group(0)  # Return the original character if limit is reached

    count = 0  # Initialize a counter for replacements
    # Use regex to find spaces, commas, or dots and replace them using the replacement function
    modified_string = re.sub(r'[ ,.]', replacement, input_string)
    
    return modified_string

# Test the function with the provided test case
assert replace_max_specialchar('Python language, Programming language.', 2) == 'Python:language: Programming language.'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_max_specialchar('Python language, Programming language.',2)==('Python:language: Programming language.')
    assert replace_max_specialchar('a b c,d e f',3)==('a:b:c:d e f')
    assert replace_max_specialchar('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')
